from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.core.serializers import serialize
from .models import *
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
import time
import json

# Create your views here.

def home_page(request):
    return render(request, 'main/index.html', {'logged':request.user.is_authenticated})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page, for example:
            print(user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            print('a')
            return render(request, 'main/login.html', {'error': 'Invalid login credentials', 'logged':request.user.is_authenticated})
    else:
        return render(request, 'main/login.html', {'logged':request.user.is_authenticated})


def register_page(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(form.cleaned_data.get('username'),
                                                form.cleaned_data.get('email'),
                                                form.cleaned_data.get('password'))
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.save()
                return redirect('login')
            else:
                form.add_error('username', 'A user with this username already exists')
        return render(request, 'main/register.html', {'form': form, 'logged':request.user.is_authenticated})
    else:
        form = AccountForm()
    return render(request, 'main/register.html', {'form': form, 'logged':request.user.is_authenticated})


@login_required
def chatrooms_page(request):
    user_chatrooms = ChatRoom.objects.all()
    if request.user.username == 'superuser':
        all_chatrooms_id = [chatroom.id for chatroom in user_chatrooms]
        all_chatrooms_lengths = [len(chatroom.members.values())+1 for chatroom in user_chatrooms]
        return render(request, 'main/chatrooms.html', {'logged':request.user.is_authenticated, 
                                                   'chatrooms':zip(all_chatrooms_id, user_chatrooms, all_chatrooms_lengths),})
    user_chatrooms = [chatroom for chatroom in user_chatrooms if request.user.username in chatroom.members.values() or request.user.username == chatroom.owner]
    user_chatrooms_id = [chatroom.id for chatroom in user_chatrooms]
    chatroom_lengths = [len(chatroom.members.values())+1 for chatroom in user_chatrooms]
    return render(request, 'main/chatrooms.html', {'logged':request.user.is_authenticated, 
                                                   'chatrooms':zip(user_chatrooms_id, user_chatrooms, chatroom_lengths),})


@login_required
def chatroom_messages(request, id):
    try:
        chatroom = get_object_or_404(ChatRoom, id=id)
    except ChatRoom.DoesNotExist:
        return HttpResponseBadRequest(content='{"error": "Chatroom does not exist"}', content_type='application/json')
    
    if request.user.username not in chatroom.members.values() and request.user.username != chatroom.owner and request.user.username != 'superuser':
        return HttpResponseBadRequest(content='{"error": "User not a member of the chatroom"}', content_type='application/json')
    
    try:
        initial_count = Text.objects.filter(chat_room=chatroom).count()
    except ObjectDoesNotExist:
        initial_count = 0
    
    start_time = datetime.now()
    timeout = timedelta(seconds=90)
    
    while datetime.now() - start_time < timeout:
        try:
            current_count = Text.objects.filter(chat_room=chatroom).count()
        except ObjectDoesNotExist:
            current_count = 0

        if initial_count != current_count:
            return JsonResponse({'reload':True})

        time.sleep(2.5)
    
    return JsonResponse([], safe=False)



@login_required
def chatroom_page(request, id):
    user_chatrooms = ChatRoom.objects.all()
    user_chatrooms = [chatroom.id for chatroom in user_chatrooms if request.user.username in chatroom.members.values() or request.user.username == chatroom.owner]
    if id in user_chatrooms or request.user.username == 'superuser':
        if request.method == 'POST':
            form = TextForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data.get('content')
                text = Text.objects.create(content=content, 
                                    author=request.user.username,
                                    chat_room=get_object_or_404(ChatRoom, id=id))
                text.save()
                return redirect('chatroom', id=id)
        chatroom_texts = Text.objects.filter(chat_room=get_object_or_404(ChatRoom, id=id))
        return render(request, 'main/chatroom.html', {'logged':request.user.is_authenticated, 'texts':chatroom_texts, "user":request.user.username, 'id':id})
    else:
        return redirect('chatrooms')
    

@login_required
def create_chatroom_page(request):
    form = ChatroomForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            usernames = {}
            for key, value in request.POST.items():
                if key.startswith('username') and value != '':
                    usernames[key] = value
            chatroom = ChatRoom.objects.create(name=name, members=usernames, owner=request.user.username)
            DeletedChatRoom.objects.create(id=chatroom.id, name=name, members=usernames, owner=request.user.username).save()
            chatroom.save()
            return redirect('chatrooms')
        return render(request, 'main/create_chatroom.html', {'logged':request.user.is_authenticated})
        
    else:
        return render(request, 'main/create_chatroom.html', {'logged':request.user.is_authenticated})


@login_required
def delete_text_page(request, chatid, textid):
    text = get_object_or_404(Text, id=textid)
    if request.user.username == text.author:
        DeletedText(id=text.id, content=text.content, author=text.author, creation_date=text.creation_date, chat_room=DeletedChatRoom.objects.get(id=chatid)).save()
        text.delete()
        return HttpResponseRedirect(reverse('chatroom', args=[chatid]))
    else:
        return redirect('chatrooms')
    


@login_required
def logout_page(request):
    logout(request)
    return redirect('login')

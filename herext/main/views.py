from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import redirect
from .forms import AccountForm
from django.contrib.auth import authenticate, login, logout

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
    user_chatrooms = [chatroom for chatroom in user_chatrooms if request.user.username in chatroom.members.values()]
    chatroom_lengths = [len(chatroom.members.values()) for chatroom in user_chatrooms]
    return render(request, 'main/chatrooms.html', {'logged':request.user.is_authenticated, 
                                                   'chatrooms':zip([(index % 3) + 1 for index in range(len(user_chatrooms))], user_chatrooms, chatroom_lengths),})


@login_required
def logout_page(request):
    logout(request)
    return redirect('login')

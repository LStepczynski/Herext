from django import forms
from django.contrib.auth.models import User
from .models import *

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ChatroomForm(forms.ModelForm):
    username1 = forms.CharField(label='Username 1', max_length=150, required=True)
    username2 = forms.CharField(label='Username 2', max_length=150, required=False)
    username3 = forms.CharField(label='Username 3', max_length=150, required=False)
    username4 = forms.CharField(label='Username 4', max_length=150, required=False)
    username5 = forms.CharField(label='Username 5', max_length=150, required=False)
    username6 = forms.CharField(label='Username 6', max_length=150, required=False)
    username7 = forms.CharField(label='Username 7', max_length=150, required=False)
    username8 = forms.CharField(label='Username 8', max_length=150, required=False)
    username9 = forms.CharField(label='Username 9', max_length=150, required=False)
    username10 = forms.CharField(label='Username 10', max_length=150, required=False)
    
    class Meta:
        model = ChatRoom
        fields = ['name', 'username1', 'username2', 'username3', 'username4', 'username5', 
                  'username6', 'username7', 'username8', 'username9', 'username10']
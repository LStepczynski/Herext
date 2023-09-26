from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home(response):
    return render(response, 'main/index.html', {})

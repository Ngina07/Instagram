from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Post
import datetime as dt

def welcome(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/register/')
def index(request):
    # current_user = request.user
    post = Posts.get_posts()

    # follow other users
    return render(request, 'index.html',{"post":post})

@login_required(login_url='/accounts/login/')
def homepage(request):
    return render(request, 'home.html')

def logout(request):
    return render(request, 'index.html')
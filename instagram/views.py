from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post


def welcome(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/register/')
def index(request):
    # current_user = request.user
    post = Posts.get_posts()

    # follow other users
    return render(request, 'index.html',{"post":post})
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Post, Follow, Comments , Profile
from .forms import PostForm, UserForm, ProfileForm
import datetime as dt




@login_required(login_url='/accounts/register/')
def index(request):
    current_user = request.user
    post = Post.get_posts()

    # follow other users
    return render(request, 'index.html',{"post":post,"user":current_user})

@login_required(login_url='/accounts/login/')
def homepage(request):
    return render(request, 'home.html')

def logout(request):
    return render(request, 'index.html')

@login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
        profile_pic = Profile.objects.filter(user_id=user).all().order_by('-id')
        post = Post.objects.filter(username_id=user).all().order_by('-id')
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'profiles/profile.html', {"post":post, "user":user, "profile_pic":profile_pic})



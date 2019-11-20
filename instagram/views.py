from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Post, Follow, Comments , Profile
from .forms import PostForm, UserForm, ProfileForm, NewCommentsForm,ProfilePicForm
from django.contrib import messages
from django.db import transaction
import datetime as dt
from vote.managers import VotableManager



votes = VotableManager()

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

@login_required
@transaction.atomic
def update_profile(request,username):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            print(request.POST['caption'])
            single_post = post_form.save(commit=False)
            single_post.username= request.user
            single_post.save()
            messages.success(request, ('Your post was successfully updated!'))
            return redirect(reverse('profiles', kwargs = {'username': request.user.username}))
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        post_form = PostForm()
    return render(request,'profiles/new_post.html', locals())

@login_required (login_url='/accounts/register/')
def comment(request,pk):
    current_user = request.user
    post = Post.get_single_post(pk)
    comments = Comments.get_post_comment(post.id)
    form = NewCommentsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.image_id = post.id
            comment.save()
            return redirect('comment')
            
        else:
            form = NewCommentsForm()
    return render(request, 'comments/new_comment.html', {"form":form, "post":post, "comments":comments})

# like a post
@login_required (login_url='/accounts/register/')
def upvote_posts(request, pk):
    post = Post.get_single_post(pk)
    user = request.user
    user_id = user.id

    if user.is_authenticated:
        upvote = post.votes.up(user_id)
        
        post.upvote_count = post.votes.count()
        post.save()
    return redirect('home')
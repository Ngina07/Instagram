from django import forms
from .models import Post, Follow, Comments , Profile
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','caption')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','website', 'bio', 'location')

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)

class NewCommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
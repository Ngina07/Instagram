from django import forms
from .models import Post, Follow, Comments , Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('image','description')
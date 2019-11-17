from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt

class Post(models.Model):
    profile_pic = models.ImageField(upload_to = 'profilepics/')
    caption = models.CharField(max_length=3000)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ImageField(upload_to='posts/')
    likes = models.IntegerField()

    
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

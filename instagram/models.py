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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'photos/',blank=True)


    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

    class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls,user_id):
        following =  Follow.objects.filter(user=user_id).all()
        return following
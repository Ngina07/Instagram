from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt


class Post(models.Model):
    image = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(max_length=3000)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    # post = models.ImageField(upload_to='posts/')
    likes = models.IntegerField()

    
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    @classmethod
    def get_posts(cls):
        post = Post.objects.all()

        return post
    @classmethod
    def get_single_post(cls, pk):
        post = cls.objects.get(pk=pk)
        return post

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField()
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


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Post)
    comment = models.CharField(max_length=150, blank=True)
    date_commented = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt
from vote.models import VoteModel
from vote.managers import VotableManager
from django.db.models.signals import post_save
from django.dispatch import receiver

#Model for Posts
class Post(VoteModel,models.Model):
    image = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(max_length=3000)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    post_date = models.DateTimeField(auto_now_add = True)
    upvote_count = models.PositiveIntegerField(default=0)

    
    
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-post_date']

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


#Model to create and edit profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField()
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'photos/',blank=True)


    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()

#Followers Model
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls,user_id):
        following =  Follow.objects.filter(user=user_id).all()
        return following


#Comments Model
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Post, on_delete=models.CASCADE )
    comment = models.CharField(max_length=150, blank=True)
    date_commented = models.DateTimeField(auto_now_add=True)

    @classmethod
    def single_comment(cls,id):
        comment = cls.objects.all()
        return comment

    @classmethod
    def get_comment(cls,id):
        comments = cls.objects.all()
        return comments

    @classmethod
    def get_post_comment(cls,pk):
        post = Post.get_single_post(pk)
        comments = []
        all_comments = Comments.objects.filter(image_id=post.id).all()
        comments += all_comments
        comment_count = len(comments)
        
        return comments
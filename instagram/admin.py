from django.contrib import admin
from .models import Profile,Post,Follow,Comments


# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Follow)
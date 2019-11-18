from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    url(r'^$', views.index,name='index'),
    url(r'^$', views.homepage,name='home'),
    url(r'^profiles/(?P<username>[-_\w.]+)$', views.profile,name='profiles'),
    url(r'^profiles/post/$', views.post,name='uploadpost'),
    url(r'^profiles/edit/(?P<username>[-_\w.]+)$', views.update_profile,name='editprofile'),
    url(r'^profiles/comment/(\d+)$', views.comment, name="comment"),
    # url(r'^update-profile-picture/(?P<username>[-_\w.]+)$', views.update_profilepic, name='update_profilepic'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
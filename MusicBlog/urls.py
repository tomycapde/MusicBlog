"""MusicBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home

from Users.views import *
from Posts.views import *
from Messages.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('login/',login_request, name='login'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('posts/', view_posts, name='view_posts'),
    path('post/<idPost>', view_single_post, name='view_single_post'),
    path('messages/', all_messages, name='messages'),
    path('new_message/', new_message, name='new_message'),
    path('chat/,<id>', chat, name='chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

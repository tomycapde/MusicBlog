from django.urls import path
from .views import view_single_post, view_posts

urlpatterns = [
    path('posts/', view_posts, name='view_posts'),
    path('post/<idPost>', view_single_post, name='view_single_post')
]
from django.urls import path
from .views import view_single_post, view_posts, edit_post, create_post

urlpatterns = [
    path('posts/', view_posts, name='view_posts'),
    path('post/<idPost>', view_single_post, name='view_single_post'),
    path('edit_post/<idPost>', edit_post, name='edit_post'),
    path('create_post/', create_post, name='create_post'),
    
]
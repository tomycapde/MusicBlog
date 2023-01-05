from django.shortcuts import render
from .models import Post
#from Users.models import Avatar
# Create your views here.


def view_single_post(request,idPost):    
    
    post = Post.objects.get(id=idPost)
    
    context = {
    'title': post.title,
    'description': post.description,
    'body': post.body,
    'author': post.author,
    'date': post.date.date,
    'image': post.image,
    'category': post.category,
    'avatar': post.author.profile.avatar,
    'bio': post.author.profile.bio,
    }
 
    return render(request, 'posts/standar_post.html', context)
    
    
def view_posts(request):
    
    posts = Post.objects.all()
    
    context = {
    'posts':posts
    }
    
    return render(request, 'posts/all_posts.html', context)

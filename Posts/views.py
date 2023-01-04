from django.shortcuts import render
from .models import Post
from Users.models import Avatar
# Create your views here.


def view_single_post(request,idPost):    
    
    post = Post.objects.get(id=idPost)

    avatar =  Avatar.objects.filter(user=post.author.id)
    
    context = {
    'title': post.title,
    'description': post.description,
    'body': post.body,
    'author': post.author,
    'date': post.date.date,
    'images': post.images,
    'category': post.category,
    'avatarurl': avatar[0].image.url,
    }
    
    print('---------------')
    print(post.images)
    print('---------------')
    print(avatar)
    print('---------------')
    
    return render(request, 'standar_post.html', context)
    
    
def view_posts(request):
    
    posts = Post.objects.all()
    
    
    context = {
    'posts':posts
    }
    
    return render(request, 'all_posts.html', context)

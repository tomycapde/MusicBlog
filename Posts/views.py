from django.shortcuts import render
from .models import Post
from .forms import PostForm

from django.views.generic import CreateView
# Create your views here.


def view_single_post(request,idPost):    
    
    post = Post.objects.get(id=idPost)
    
    if post.author.profile.avatar:
        avatar = post.author.profile.avatar
    else:
        avatar = "avatars/user-logo.png"
    
    context = {
    'title': post.title,
    'description': post.description,
    'body': post.body,
    'author': post.author,
    'date': post.date.date,
    'image': post.image,
    'category': post.category,
    'avatar': avatar,
    'bio': post.author.profile.bio,
    'id':post.id,
    }
 
    return render(request, 'posts/standar_post.html', context)
    
    
def view_posts(request):
    
    posts = Post.objects.all()
    
    context = {
    'posts':posts
    }
    
    return render(request, 'posts/all_posts.html', context)

'''
def edit_post(request, idPost):
    
    post = Post.objects.get(id=idPost)
    
    form = PostForm()
    
    
    context = {
        'form':form,
    }
    
    return render(request, 'posts/edit_post.html', context)
    
    '''
    
def edit_post(CreateView):
    model = Post
    template_name = 'post/edit_post.html'
    fields = '__all__'
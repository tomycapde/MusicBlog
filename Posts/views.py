from django.shortcuts import render
from .models import Topic, Post
# Create your views here.


def mostrar_post(request):
    post = Topic.objects.get() 
    
    return render(request, 'prueba_post.html', {'title': post.title,'content':post.content})

def mostrar_post2(request):
    post = Post.objects.get()
    
    context = {
        'title': post.title,
        'description': post.description,
        'body': post.body,
        'author': post.author,
        'date': post.date,
        'content': post.content
    }
    
    return render(request, 'prueba_post.html', context)
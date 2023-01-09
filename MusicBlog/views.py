from django.shortcuts import render
from Posts.models import Post

def home(request):
    
    posts = Post.objects.all() 
    number_posts = len(posts)
    
    post1 = posts[number_posts - 1]
    post2 = posts[number_posts - 2]
    post3 = posts[number_posts - 3]
    
    context = {
        'post1': post1,
        'post2': post2,
        'post3': post3,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'acerca_de.html')
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post
# Create your views here.

# class BlogListView(ListView):
#     model = Post
#
#     template_name = 'index.html'

menu = {'Blog': "home", 'Add article': "home"}

def index(request):
    posts = Post.objects.all()
    activ = 1
    
    return render(request, 'main/index.html', {"posts": posts, "menu": menu})

def show_post(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/blog_post.html', {"post": post, "menu": menu})
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

# class BlogListView(ListView):
#     model = Post
#
#     template_name = 'index.html'

menu = {'Blog': "home", 'Add article': "home"}

def index(request):
    posts = Post.objects.all()[:5]
    comments = Comment.objects.all()
    
    return render(request, 'main/index.html', {"posts": posts, "menu": menu})


def show_post(request, post_id):

    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post_id=post_id, is_active=True)
    all_comments_post = len(comments)
    initial = {'post': post.pk}
    form = CommentForm(initial=initial)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            print(c_form.cleaned_data)
            c_form.save()
        else:
            form = c_form
    else:
        form = CommentForm()
    data = {
        'post': post,
        'menu': menu,
        'commentform': form,
        'comments': comments,
        'all_comm': all_comments_post,
    }
    return render(request, 'main/blog_post.html', data)

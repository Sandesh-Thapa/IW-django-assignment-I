from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'blog/landing.html', {})


def posts(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'all_blogs': all_blogs})


def post_detail(request, x):
    obj = Blog.objects.get(slug=x)
    # context = {
    #     'title': obj.title,
    #     'author': obj.author,
    #     'created_at': obj.created_at,
    #     'body': obj.body
    # }
    context = {
        'obj': obj
    }
    return render(request, 'blog/post.html', context)

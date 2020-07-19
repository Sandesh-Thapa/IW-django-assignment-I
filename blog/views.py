from django.shortcuts import render
from .models import Blog


# Create your views here.
def home(request):
    return render(request, 'blog/landing.html', {})


def posts(request):
    all_blogs = Blog.objects.all()
    context = {'all_blogs': all_blogs}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    obj = Blog.objects.get(id=id)
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

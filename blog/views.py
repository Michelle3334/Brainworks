"Blog app views"
from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    """ A view to return the blog list page"""
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_post.html', context)


def blog_detail(request, blog_id):
    """ A view to show blog details """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)

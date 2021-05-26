from django.shortcuts import render
from .models import BlogPost


def index(request):
    """The home page for Blog. It shows the sorted list of posts in the blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import PostForm


def index(request):
    """The home page for Blog. It shows the sorted list of posts in the blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    title = post.title
    text = post.text

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post.
        form = BlogPost(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'title': title, 'text': text, 'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

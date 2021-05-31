from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import PostForm


def index(request):
    """The home page for Blog. It shows the sorted list of posts in the blog."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save('new_post')
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    check_post_owner(request, post)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)


def check_post_owner(request, post):
    # Make sure the post belong to the current user.
    if post.owner != request.user:
        raise Http404

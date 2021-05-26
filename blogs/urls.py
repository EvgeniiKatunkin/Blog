"""Defines URL patterns for blogs."""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),

    # Page for editing existing posts
    path('edit_post/', views.edit_post, name='edit_post'),
]

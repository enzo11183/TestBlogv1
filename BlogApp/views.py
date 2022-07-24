from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model= Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

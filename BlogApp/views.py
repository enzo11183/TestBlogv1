from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView, TemplateView

from django.db import models
from django.db.models import Model
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime

def kaydet(request):
    dmetin = request.POST['tmetin']
    dbaslik = request.POST['baslik']
    dslug = request.POST['slug']
    

    tempPost = Post()
    tempPost.author =  User.objects.get(username='admin')
    tempPost.title = dbaslik
    tempPost.body = dmetin
    tempPost.slug = dslug
    tempPost.publish = datetime.datetime.now()
    tempPost.save()
    return render(request, 'kaydet.html')

def createPage(request):
    

    context = {}
    return render(request, 'create.html', context)


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model= Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

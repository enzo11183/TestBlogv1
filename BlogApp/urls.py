from django.urls import path
from .views import BlogListView, BlogDetailView
from . import views

from django.views.generic import RedirectView

app_name = 'BlogApp'
urlpatterns = [
    # post views
    path('', RedirectView.as_view(url='/main'), name='index'),
    path('main/', BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
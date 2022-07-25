from django.urls import path
from .views import BlogListView, BlogDetailView
from . import views

from django.views.generic import RedirectView

app_name = 'BlogApp'
urlpatterns = [
    # post views
    path('', RedirectView.as_view(url='main'), name='main'),
    path('main/', BlogListView.as_view(), name='blog_list'),
    path('create/', views.createPage, name='create'),
    path('kaydet/',views.kaydet, name = 'kaydet'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    
]
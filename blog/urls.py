from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.Blog.as_view(), name='blog'),
    path('create/', views.CreateBlogView.as_view(), name='create'),
    path('blogpost/<slug>/', views.BlogPostView.as_view(), name='blogpost'),
]
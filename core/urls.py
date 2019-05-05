from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='home'),
    #path('blog/', Blog.as_view(), name='blog'),
    #path('crypto/', crypto, name='crypto'),
]
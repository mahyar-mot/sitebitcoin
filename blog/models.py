from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogTag(models.Model):
    tagname = models.CharField(max_length=20)
    def __str__(self):
        return self.tagname

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blogtag = models.ForeignKey(BlogTag , on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='de.jpg',blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    def snippet(self):
        return self.body[:150]

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_commented = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.blog_post.title)+str(self.commenter)
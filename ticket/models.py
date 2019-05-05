from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    close = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{}-{}'.format(self.title, self.id)

    def get_absolute_url(self):
        return reverse('ticketapp:ticketdetail', kwargs={'category':self.category.slug, 'pk':self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Messages(models.Model):
    created_ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ticketapp:ticketdetail', kwargs={'category':self.created_ticket.category.slug, 'pk':self.created_ticket.pk})

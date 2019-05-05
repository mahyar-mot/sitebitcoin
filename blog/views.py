from django.shortcuts import redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms


class Blog(ListView):
    template_name = "blog.html"
    model = models.BlogPost
    context_object_name = 'blogpost'


class BlogPostView(DetailView):
    model = models.BlogPost
    template_name = 'blogpost.html'
    def post(self, request, **kwargs):
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.blog_post = models.BlogPost.objects.get(slug=self.kwargs['slug'])
            if request.user.is_authenticated:
                temp.commenter = request.user
            temp.save()
            return redirect('blogapp:blogpost')
        else:
            return HttpResponse('fail')



class CreateBlogView(LoginRequiredMixin, CreateView):
    model = models.BlogPost
    template_name = 'createblog.html'
    form_class = forms.NewBlogForm

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        return super().form_valid(form)

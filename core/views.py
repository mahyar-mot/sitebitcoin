
from django.views.generic import TemplateView
from blog import models



class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = models.BlogPost.objects.all()[:3]
        return context
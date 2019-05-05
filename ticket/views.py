from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from extra_views import ModelFormSetView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from . import models
from . import forms


class NewTicketView(LoginRequiredMixin, CreateView):
    model = models.Ticket
    template_name = 'ticketapp/newticket.html'
    form_class = forms.NewTicketForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketDetailView(LoginRequiredMixin, CreateView, DetailView):
    model = models.Ticket
    template_name = 'ticketapp/ticketdetail.html'
    form_class = forms.MessageForm

    def form_valid(self, form, **kwargs):
        form.instance.created_ticket = models.Ticket.objects.get(category__slug=self.kwargs['category'],
                                                                 pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)


class SupportView(LoginRequiredMixin, ListView):
    template_name = 'ticketapp/support.html'
    context_object_name = 'created_ticket'

    def get_queryset(self):
        return models.Ticket.objects.filter(user=self.request.user)


@method_decorator(staff_member_required, name='dispatch')
class TicketsListView(LoginRequiredMixin, ModelFormSetView):
    model = models.Ticket
    template_name = 'ticketapp/ticketslist.html'
    fields = ['close']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ctx = models.Ticket.objects.all()
        context['tickets'] = zip(self.construct_formset(), ctx)
        return context

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs['extra'] = 0
        return kwargs


@method_decorator(staff_member_required, name='dispatch')
class TicketsListViewOpen(LoginRequiredMixin, ModelFormSetView):
    model = models.Ticket
    template_name = 'ticketapp/ticketslist.html'
    fields = ['close']

    def get_queryset(self):
        return models.Ticket.objects.all().filter(close=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ctx = models.Ticket.objects.all()
        context['tickets'] = zip(self.construct_formset(), ctx)
        return context

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs['extra'] = 0
        return kwargs


@method_decorator(staff_member_required, name='dispatch')
class TicketsListViewClose(LoginRequiredMixin, ModelFormSetView):
    model = models.Ticket
    template_name = 'ticketapp/ticketslist.html'
    fields = ['close']

    def get_queryset(self):
        return models.Ticket.objects.all().filter(close=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ctx = models.Ticket.objects.all()
        context['tickets'] = zip(self.construct_formset(), ctx)
        return context

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs['extra'] = 0
        return kwargs


# def TicketsListView(request):
#     formset = forms.EditTicketFormSet()
#     context = models.Ticket.objects.all()
#     both = zip(formset,context)
#     return render(request, 'ticketapp/ticketslist.html',{'both':both})

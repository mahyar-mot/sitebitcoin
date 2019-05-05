from django.shortcuts import render , HttpResponse , redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login ,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from . import forms

# Create your views here.
class Profile_View(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class SignUp_View(CreateView):
    form_class = forms.SignUpForm
    template_name = 'signup.html'
    success_url = '/accounts/login'


class SignIn_View(FormView):
    form_class = forms.LoginForm
    template_name = 'login.html'
    success_url = '/accounts/profile'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class SignOut_View(TemplateView):
    def post(self,request):
        logout(request)
        return redirect('home')

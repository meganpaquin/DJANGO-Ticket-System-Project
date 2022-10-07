from pipes import Template
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from accounts.models import Usernames
from django.contrib.auth.models import User
from django.views.generic import TemplateView

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

 

class ManagerPageView(TemplateView):
    template_name = "accounts/users.html"

    def get_context_data(self, **kwargs):
        user_model = User.objects.all()
        context = super().get_context_data(**kwargs)
        context["user_list"] = user_model
        return context




    


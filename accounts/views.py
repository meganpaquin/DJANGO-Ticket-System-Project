from audioop import reverse
from pipes import Template
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from accounts.models import Usernames
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserChangeForm
from tickets.models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

 

class ManagerPageView(TemplateView):
    template_name = "accounts/users.html"

    def set_staff(self):
        staff = self.request
        return staff

    def get_context_data(self, **kwargs):
        user_model = User.objects.all()
        context = super().get_context_data(**kwargs)
        context["user_list"] = user_model

        ticket_model = Ticket.objects.all()
        context["ticket_list"] = ticket_model.filter().order_by('created_on').reverse()

        return context


class UserChangeView(UpdateView):
    template_name = 'registration/change_user.html'
    form_class = UserChangeForm
    model = User




    


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TicketListView(ListView):
    template_name = "tickets/list.html"
    model = Ticket


class TicketDetailView(DetailView):
    template_name = "tickets/detail.html"
    model = Ticket

class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = "tickets/new.html"
    model = Ticket
    fields = ["title", "description"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "tickets/update.html"
    model = Ticket
    fields = ["title", "description", "status"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user

class TicketDelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "tickets/delete.html"
    model = Ticket
    success_url = reverse_lazy("list")
    
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


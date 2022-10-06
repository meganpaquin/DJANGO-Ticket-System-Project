from django.views.generic import TemplateView
from tickets.models import Ticket

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
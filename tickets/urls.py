from django.urls import path
from .views import TicketListView, TicketDelView, TicketCreateView, TicketUpdateView, TicketDetailView

urlpatterns = [
    path('tickets/', TicketListView.as_view(), name="tickets"),
    path('<int:pk>', TicketDetailView.as_view(), name="detail"),
    path('<int:pk>/delete', TicketDelView.as_view(), name="delete"),
    path('<int:pk>/edit', TicketUpdateView.as_view(), name="update"),
    path('new/', TicketCreateView.as_view(), name="new"),
]
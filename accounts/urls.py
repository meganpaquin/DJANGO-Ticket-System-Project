from django.urls import path
from .views import SignUpView, ManagerPageView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', ManagerPageView.as_view(), name="users"),
]
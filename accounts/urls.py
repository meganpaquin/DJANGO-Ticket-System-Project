from django.urls import path
from .views import SignUpView, ManagerPageView, UserChangeView, UserChangeView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', ManagerPageView.as_view(), name="users"),
    path('users/<int:pk>/edit', UserChangeView.as_view(), name="change_user"),
]
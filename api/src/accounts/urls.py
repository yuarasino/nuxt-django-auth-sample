from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

app_name = "accounts"

urlpatterns = [
    path("login", ObtainAuthToken.as_view(), name="login"),
    path("user", views.UserView.as_view(), name="user"),
    path("hello", views.HelloView.as_view(), name="hello"),
]

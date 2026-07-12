from django.urls import path
from . import views 

app_name = "accounts"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("register/", views.register_request, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_request, name="logout"),
]
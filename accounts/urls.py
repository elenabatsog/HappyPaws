from django.urls import path
from . import views 

app_name = "accounts"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register_request, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/edit/", views.edit_profile, name="edit_profile")
]
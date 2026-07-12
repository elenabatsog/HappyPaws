from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls")),
    path("shelter/", include("shelter.urls")),
    path('admin/', admin.site.urls),
]



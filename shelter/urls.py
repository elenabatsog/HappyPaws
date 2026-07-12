from django.urls import path 
from . import views

app_name = "shelter"

urlpatterns = [
    path("animals/", views.browse_animals, name="browse_animals"),
    path("favourites/", views.favourites, name="favourites"),
    path("suggest/", views.suggest_animal, name="suggest_animal"),
    path("manage/", views.manage_animals, name="manage_animals"),
]
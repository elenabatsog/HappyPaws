from django.urls import path 
from . import views

app_name = "shelter"

urlpatterns = [
    path("animals/", views.browse_animals, name="browse_animals"),
    path("favourites/", views.favourites, name="favourites"),
    path("animals/<int:pet_id>/favourite/", views.toggle_favourite, name="toggle_favourite"),
    path("suggest/", views.suggest_animal, name="suggest_animal"),
    path("my-suggestions/", views.my_suggestions, name="my_suggestions"),
    path("manage/", views.manage_animals, name="manage_animals"),
    path("animals/<int:pet_id>/", views.pet_details, name="pet_details"),
]
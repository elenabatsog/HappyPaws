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
    path("manage/add", views.add_pet, name="add_pet"),
    path("manage/<int:pet_id>/edit/", views.edit_pet, name="edit_pet"),
    path("manage/<int:pet_id>/delete/", views.delete_pet, name="delete_pet"),
    path("animals/<int:pet_id>/", views.pet_details, name="pet_details"),
    path("admin-tools/suggestions/", views.admin_suggestions, name="admin_suggestions"),
    path("admin-tools/suggestions/<int:suggestion_id>/approve/", views.approve_suggestion, name="approve_suggestion"),
    path("admin-tools/suggestions/<int:suggestion_id>/reject/", views.reject_suggestion, name="reject_suggestion"),

]
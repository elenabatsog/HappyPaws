from django.contrib import admin
from .models import Category, Favourite, Pet

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "breed",
        "age",
        "gender",
        "size",
        "status",
        "vaccinated",
    ]

    list_filter = [
        "category",
        "gender",
        "size",
        "status",
        "vaccinated",
    ]

    search_fields = [
        "name",
        "breed",
    ]

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "pet",
        "created_at",
    ]

    search_fields = [
        "user__email",
        "pet__name",
    ]

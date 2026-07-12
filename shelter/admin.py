from django.contrib import admin
from .models import Category, Pet

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

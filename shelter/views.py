from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Pet

@login_required
def browse_animals(request):
    pets = Pet.objects.all().order_by("-created_at")

    return render(
        request,
        "shelter/browse_animals.html",
        {"pets": pets},
    )

@login_required
def favourites(request):
    return render(request, "shelter/favourites.html")

@login_required
def suggest_animal(request):
    return render(request, "shelter/suggest_animal.html")

@login_required
def manage_animals(request):
    return render(request, "shelter/manage_animal.html")
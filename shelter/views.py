from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Favourite, Pet

@login_required
def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    is_favourite = Favourite.objects.filter(
        user= request.user,
        pet=pet,
    ).exists()

    return render(
        request,
        "shelter/pet_details.html",
        {
            "pet": pet,
            "is_favourite": is_favourite,
        },
    )


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
    favourite_items = Favourite.objects.filter(
        user = request.user
    ).select_related("pet")
    return render(request, "shelter/favourites.html", {"favourite_items": favourite_items})

@login_required
def suggest_animal(request):
    return render(request, "shelter/suggest_animal.html")

@login_required
def manage_animals(request):
    return render(request, "shelter/manage_animal.html")

@login_required
def toggle_favourite(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == "POST":
        favourite = Favourite.objects.filter(
            user = request.user,
            pet=pet,
        ).first()

        if favourite:
            favourite.delete()
        else:
            Favourite.objects.create(
                user=request.user,
                pet=pet,
            )

    return redirect("shelter:pet_details", pet_id=pet.id)
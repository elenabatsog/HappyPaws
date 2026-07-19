from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AnimalSuggestionForm, PetForm, AdoptionRequestForm, ReviewForm
from .models import AnimalSuggestion, Category, Favourite, Pet, CartItem, Review
from django.db.models import Q 

@login_required
def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    is_favourite = Favourite.objects.filter(
        user= request.user,
        pet=pet,
    ).exists()
    
    likes_count = Favourite.objects.filter(
            pet=pet,
        ).count()
    
    recommended_pets = Pet.objects.filter(
        category=pet.category,
        status="AVAILABLE",
    ).exclude(
        id=pet.id,
    )[:3]

    reviews = Review.objects.filter(
        pet=pet,
    ).order_by("-created_at")

    existing_review = Review.objects.filter(
        user=request.user,
        pet=pet,
    ).first()

    if request.method == "POST":
        review_form = ReviewForm(
            request.POST,
            instance = existing_review,
        )

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.pet = pet
            review.save()

            messages.success(
                request,
                "Your review was saved successfully. "
            )

            return redirect(
                "shelter:pet_details",
                pet_id = pet.id,
            )
    else:
        review_form = ReviewForm(
            instance = existing_review,
        )

    return render(
        request,
        "shelter/pet_details.html",
        {
            "pet": pet,
            "is_favourite": is_favourite,
            "likes_count": likes_count,
            "recommended_pets": recommended_pets,
            "reviews": reviews,
            "review_form": review_form,
            "existing_review": existing_review,
        },
    )

@login_required
def browse_animals(request):
    pets = Pet.objects.filter(
        status="AVAILABLE"
    )

    search = request.GET.get("search", "")  

    category = request.GET.get("category", "")
    
    gender = request.GET.get("gender", "")

    size = request.GET.get("size", "")

    vaccinated = request.GET.get("vaccinated", "")

    if search:
        pets = pets.filter(
            Q(name__icontains=search) |
            Q(breed__icontains=search)
        )

    if category:
        pets = pets.filter(
            category_id=category
        )
    
    if gender:
        pets = pets.filter(
            gender=gender
        )
    
    if size:
        pets = pets.filter(
            size=size
        )
    
    if vaccinated == "yes":
        pets = pets.filter(
            vaccinated=True
        )
    elif vaccinated == "no":
        pets = pets.filter(
            vaccinated=False
        )
    
    categories = Category.objects.all()

    return render(
        request,
        "shelter/browse_animals.html",
        {
            "pets": pets,
            "categories": categories,
            "search": search,
            "selected_category": category,
            "selected_gender": gender,
            "selected_size": size,
            "selected_vaccinated": vaccinated,
        },
    )

@login_required
def favourites(request):
    favourite_items = Favourite.objects.filter(
        user = request.user
    ).select_related("pet")
    return render(request, "shelter/favourites.html", {"favourite_items": favourite_items})

@login_required
def suggest_animal(request):
    form = AnimalSuggestionForm(
        request.POST,
        request.FILES,
    )

    if form.is_valid():
        suggestion = form.save(commit=False)

        suggestion.submitted_by = request.user
        suggestion.status = "PENDING"

        suggestion.save()

        messages.success(
            request,
            "Your animal suggestion was submitted successfully."
        )

        return redirect("shelter:my_suggestions")
    else:
        form = AnimalSuggestionForm()
    
    return render(request, "shelter/suggest_animal.html", {"form": form})

@login_required
def my_suggestions(request):
    suggestions = AnimalSuggestion.objects.filter(
        submitted_by=request.user
    ).order_by("-submitted_at")

    return render(
        request,
        "shelter/my_suggestions.html",
        {"suggestions": suggestions},
    )

@login_required
def manage_animals(request):
    if request.user.profile.role not in ["ORGANIZATION", "ADMIN"]:
        messages.error(
            request,
            "You do not have permission to manage animals.",
        )

        return redirect("accounts:dashboard")
    
    pets = Pet.objects.all().order_by("-created_at")

    return render(request, "shelter/manage_animals.html", {"pets": pets})

@login_required
def add_pet(request):
    if request.user.profile.role not in ["ORGANIZATION", "ADMIN"]:
        messages.error(
            request,
            "You do not have permission to add animals. ",
        )

        return redirect("accounts:dasboard")
    
    form = PetForm()

    if request.method == "POST":
        form = PetForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            pet = form.save(commit=False)

            pet.created_by = request.user
            pet.save()

            messages.success(
                request,
                "Animal added successfully! ",
            )

            return redirect("shelter:manage_animals")
        
    return render(
        request,
        "shelter/pet_form.html",
        {
            "form": form,
            "page_title": "Add Animal",
            "button_text": "Add Animal",
        },
    )

@login_required
def edit_pet(request, pet_id):
    if request.user.profile.role not in ["ORGANIZATION", "ADMIN"]:
        messages.error(
            request,
            "You do not have permission to edit animals. ",
        )

        return redirect("accounts:dasboard")
    
    pet = get_object_or_404(
        Pet,
        id=pet_id,
    )
    
    form = PetForm(instance=pet)

    if request.method == "POST":
        form = PetForm(
            request.POST,
            request.FILES,
            instance=pet,
        )

        if form.is_valid():
            pet.save()

            messages.success(
                request,
                "Animal updated successfully! ",
            )

            return redirect("shelter:manage_animals")
        
    return render(
        request,
        "shelter/pet_form.html",
        {
            "form": form,
            "page_title": "Edit Animal",
            "button_text": "Save Changes",
        },
    )

@login_required
def delete_pet(request, pet_id):
    if request.user.profile.role not in ["ORGANIZATION", "ADMIN"]:
        messages.error(
            request,
            "You do not have permission to delete animals. ",
        )

        return redirect("accounts:dasboard")
    
    pet = get_object_or_404(
        Pet,
        id=pet_id,
    )

    if request.method == "POST":
        pet.delete()

        messages.success(
            request,
            "Animal deleted successfully! ",
        )

        return redirect("shelter:manage_animals")
        
    return render(
        request,
        "shelter/delete_pet.html",
        {"pet": pet},
    )



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

@login_required
def admin_suggestions(request):
    if request.user.profile.role != "ADMIN":
        messages.error(
            request,
            "You do not have permission to access admin tools. ",
        )

        return redirect("accounts:dashboard")
    
    suggestions = AnimalSuggestion.objects.all().order_by(
        "-submitted_at"
    )

    return render(
        request,
        "shelter/admin_suggestions.html",
        {"suggestions": suggestions},
    )

@login_required
def approve_suggestion(request, suggestion_id):
    if request.user.profile.role != "ADMIN":
        messages.error(
            request,
            "You do not have permission to access admin tools. ",
        )

        return redirect("accounts:dashboard")
    
    suggestion = get_object_or_404(
        AnimalSuggestion,
        id=suggestion_id,
    )

    if request.method == "POST":
        suggestion.status = "APPROVED"
        suggestion.reviewed_by = request.user
        suggestion.rejection_reason = ""
        
        Pet.objects.create(
            name=suggestion.animal_name if suggestion.animal_name else suggestion.animal_type,
            category=Category.objects.get(
                name__iexact=suggestion.animal_type
            ),

            breed=suggestion.breed,
            age=suggestion.estimated_age if suggestion.estimated_age else 0,
            description=suggestion.description,
            image=suggestion.image,
            created_by=request.user,
        )
        
        suggestion.save()

        messages.success(
            request,
            "Suggestion approved and animal saved successfully! ",
        )

    return redirect("shelter:admin_suggestions")

@login_required
def reject_suggestion(request, suggestion_id):
    if request.user.profile.role != "ADMIN":
        messages.error(
            request,
            "You do not have permission to access admin tools. ",
        )

        return redirect("accounts:dashboard")
    
    suggestion = get_object_or_404(
        AnimalSuggestion,
        id=suggestion_id,
    )

    if request.method == "POST":
        rejection_reason = request.POST.get(
            "rejection_reason",
            "",
        )

        suggestion.status = "REJECTED"
        suggestion.reviewed_by = request.user
        suggestion.rejection_reason = rejection_reason
        suggestion.save()

        messages.success(
            request,
            "Suggestion rejected successfully! ",
        )

        return redirect("shelter:admin_suggestions")

    return render(
        request,
        "shelter/reject_suggestion.html",
        {"suggestion": suggestion},
    )
        
@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(
        Pet,
        id=pet_id,
        status="AVAILABLE"
    )

    if request.method == "POST":
        form = AdoptionRequestForm(request.POST)

        if form.is_valid():
            adoption_request = form.save(commit=False)

            adoption_request.user = request.user
            adoption_request.pet = pet

            adoption_request.save()

            return redirect( "shelter:adoption_success", pet_id=pet.id)
    else:
        form = AdoptionRequestForm(
            initial={
                "full_name": request.user.get_full_name(),
                "email": request.user.email,
            }
        )

    context = {
        "pet": pet,
        "form": form,
    }

    return render(
        request,
        "shelter/adopt_pet.html",
        context,
    )
    
@login_required
def adoption_success(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    return render(
        request,
        "shelter/adoption_success.html",
        {"pet": pet}
    )

@login_required
def add_to_cart(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    CartItem.objects.get_or_create(
        user = request.user,
        pet = pet,
    )

    return redirect("shelter:view_cart")

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(
        user=request.user
    )

    return render(
        request,
        "shelter/cart.html",
        {"cart_items": cart_items},
    )

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id = item_id,
        user = request.user
    )

    cart_item.delete()

    return redirect("shelter:view_cart")

@login_required
def submit_cart(request):
    CartItem.objects.filter(
        user=request.user
    ).delete()

    return render(
        request,
        "shelter/cart_success.html",
    )
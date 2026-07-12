from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import UserProfile

from . forms import LoginForm, NewUserForm 

def welcome(request):
    """Display the HappyPaws login page."""

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"].lower()
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=email,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("accounts:dashboard")
            
            messages.error(
                request,
                "The email or password is incorrect.",
            )
    
    return render(
        request,
        "accounts/welcome.html",
        {"login_form": form},
    )

def register_request(request):
    """Create a new regular user account"""

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            #users cannot choose their own role. preventing them from registering as an admin.
            UserProfile.objects.create(
                user=user,
                role="USER",
            )

            login(request,user)

            messages.success(
                request,
                "Your account was created successfully!",
            )

            return redirect("accounts:dashboard")

    return render(
        request,
        "accounts/register.html",
        {"register_form": form},
    )

@login_required
def dashboard(request):
    """Display the shared dashboard after authentication."""

    return render(request, "accounts/dashboard.html")

@login_required
def logout_request(request):
    """Log out with security"""

    if request.method == "POST":
        logout(request)
        messages.success(request, "You have logged out successfully!")

    return redirect("accounts:welcome")



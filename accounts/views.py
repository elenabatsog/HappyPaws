from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . forms import NewUserForm 

def welcome(request):
    """Display the HappyPaws welcome page."""

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    
    return render(request, "accounts/welcome.html")

def register_request(request):
    """Create a new regular user account"""

    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)

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



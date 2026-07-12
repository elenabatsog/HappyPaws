from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    email = forms.EmailField(
        label = "Email Address",
        widget=forms.EmailInput (
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
            }
        ),
    )

class NewUserForm(UserCreationForm):
    """Form used to create a new HappyPaws user."""

    first_name = forms.CharField (
        max_length = 150,
        required = True,
        label="First Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your first name",
            }
        ),
    )

    last_name = forms.CharField(
        max_length = 150,
        required = True,
        label = "Last Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your last name",
            }
        ),
    )

    email = forms.EmailField (
        required = True,
        label = "Email Address",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Create a password",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Confirm your password",
            }
        )

    def clean_email(self):
        """Check that another account does not already use the email"""

        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )
        
        return email 
    
    def save(self, commit=True):
        """Save the new user and use their email as their username."""

        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        user.username = user.email

        if commit:
            user.save()

        return user 
    
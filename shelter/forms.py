from django import forms
from .models import AnimalSuggestion, Pet, AdoptionRequest, Review

class AnimalSuggestionForm(forms.ModelForm):
    class Meta:
        model = AnimalSuggestion

        fields = [
            "animal_name",
            "animal_type",
            "breed",
            "estimated_age",
            "location_found",
            "description",
            "image",
        ]

        widgets = {
            "animal_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "animal_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Dog, cat, rabbit, bird"
                }
            ),

            "breed": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "estimated_age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),

            "location_found": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),


        }

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = [
            "name",
            "category",
            "breed",
            "age",
            "gender",
            "size",
            "description",
            "adoption_fee",
            "vaccinated",
            "status",
            "image",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "category": forms.Select(
                attrs={"class": "form-select"}
            ),

            "breed": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),

            "gender": forms.Select(
                attrs={"class": "form-control"}
            ),

            "size": forms.Select(
                attrs={"class": "form-select"}
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),

            "adoption_fee": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "step": "0.01",
                    }
            ),

            "vaccinated": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

            "status": forms.Select(
                attrs={"class": "form-control"}
            ),

            "image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest

        fields = [
            "full_name",
            "email",
            "phone_number",
            "address",
            "reason",
        ]

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your full name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email address",
                }
            ),

            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your home address",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Why would you like to adopt this animal?",
                }
            ),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = [
            "rating",
            "comment",
        ]

        widgets = {
            "rating": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write your review..",
                }
            ),
        }
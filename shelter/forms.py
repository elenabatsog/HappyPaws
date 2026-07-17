from django import forms
from .models import AnimalSuggestion, Pet

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
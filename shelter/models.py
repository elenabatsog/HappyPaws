from django.contrib.auth.models import User 
from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, 
    )

    def __str__(self):
        return self.name 
    
class Pet(models.Model):
    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    ]

    SIZE_CHOICES = [
        ("SMALL", "Small"),
        ("MEDIUM", "Medium"),
        ("LARGE", "Large"),
    ]

    STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("RESERVED", "Reserved"),
        ("ADOPTED", "Adopted"),
    ]

    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="pets",
    )

    breed = models.CharField(
        max_length=100,
        blank=True
    )

    age = models.PositiveBigIntegerField(
        help_text="Age in years",
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
    )

    description = models.TextField()

    adoption_fee = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0,
    )

    vaccinated = models.BooleanField(
        default=False,
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="AVAILABLE",
    )

    image = models.ImageField(
        upload_to = "pets/",
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_pets",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} - {self.category.name}"


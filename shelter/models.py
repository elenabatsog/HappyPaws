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
    
class Favourite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favourites",
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="favourited_by",
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
    )

    class Meta:
        #it prevents the same user from tapping the same animal two times, each pet is unique
        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                name = "unique_user_pet_favourite",
            )
        ]

    def __str__(self):
        return f"{self.user.email} likes {self.pet.name}"

class AnimalSuggestion(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    submitted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="animal_suggestions",
    )

    animal_name = models.CharField(
        max_length=100,
        blank=True,
    )

    animal_type = models.CharField(
        max_length=50,
    )

    breed = models.CharField(
        max_length=100,
        blank=True,
    )

    estimated_age = models.PositiveBigIntegerField(
        blank=True,
        null=True,
        help_text="Estimated age in years",
    )

    location_found = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to = "suggestions/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    rejection_reason = models.TextField(
        blank=True,
    )

    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_suggestions",
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.animal_type} - {self.get_status_display()}"
    
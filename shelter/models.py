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

class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected")
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="adoption_requests",
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="adoption_requests",
    )

    full_name = models.CharField(
        max_length=150,
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=30,
    )

    address = models.CharField(
        max_length=255,
    )

    reason = models.TextField(
        help_text="Explain the reason why you would like to adopt this animal in a few words."
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user.email} - {self.pet.name} - {self.get_status_display()}"
    
class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                name="unique_cart_item",
            )
        ]

        def __str__(self):
            return f"{self.user.email} - {self.pet.name}"
        
class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.IntegerField(
        choices=[
            (1, "1 Star"),
            (2, "2 Star"),
            (3, "3 Star"),
            (4, "4 Star"),
            (5, "5 Star"),
        ]
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                name="one_review_per_user_pet",
            )
        ]

        def __str__(self):
            return f"{self.user.username} - {self.pet.name}"


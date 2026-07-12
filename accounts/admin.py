from django.contrib import admin
from .models import UserProfile 

#the administrator can view and change roles through admin panel
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "role", "phone"]
    list_filter = ["role"]
    search_fields = ["user__email", "user__first_name", "user__last_name"]

from django.contrib import admin

from ..models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin[User]):
    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")
    ordering = ("id",)

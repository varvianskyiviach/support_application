from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ["groups", "user_permissions"]
    readonly_fields = [
        "password",
        "date_joined",
        "is_superuser",
        "is_staff",
        "is_active",
        "email",
        "last_login",
    ]
    list_display = ["email", "first_name", "last_name", "role", "is_active"]
    search_fields = ["email"]
    list_filter = ["role"]

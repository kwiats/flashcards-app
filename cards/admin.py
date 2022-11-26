from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Word, Category, User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                )
            },
        ),
        (
            "Advanced options",
            {"fields": ("profile_picture",)},
        ),
    )


admin.site.register(Word)
admin.site.register(Category)

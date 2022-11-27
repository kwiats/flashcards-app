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


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "translated_word")


admin.site.register(Category)

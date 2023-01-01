from django.contrib import admin
from .models import Word, Translation, Category
import re


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    ordering = ("id",)

    list_display = (
        "id",
        "word",
        "user",
        "status",
    )


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    ordering = ("-updated",)

    list_display = ("id", "word", "translation", "pronunciation")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "price",
        "user",
        "amount",
    )
    ordering = ("id",)

    def user(self, obj):
        return ", ".join([user.username for user in obj.users.all()])

    def amount(self, obj):
        return len(obj.users.all())

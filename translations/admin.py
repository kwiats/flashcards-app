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
        "isDefault",
        "category",
        "price",
        "user",
        "amount",
    )
    ordering = ("id",)

    def isDefault(self, obj):
        # Utwórz wyrażenie regularne dla słowa i dodaj flagę IGNORECASE
        regex = r"\b{}\b".format("default")
        pattern = re.compile(regex, flags=re.IGNORECASE)
        # Sprawdź, czy łańcuch zawiera słowo za pomocą metody search()
        if pattern.search(obj.category):
            return True
        return False

    def user(self, obj):
        return ", ".join([user.username for user in obj.users.all()])

    def amount(self, obj):
        return len(obj.users.all())

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _


from .models import Word, Category, User, Ranking
import re


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "current_score",
        "total_score",
    )
    search_fields = ("username",)
    ordering = ("-total_score",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "profile_picture",
                    "total_score",
                    "current_score",
                    "spend_score",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "profile_picture",
                ),
            },
        ),
    )


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    ordering = ("id",)

    list_display = (
        "id",
        "word",
        "translated_word",
        "user",
        "status",
    )


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


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = (
        "ranking_name",
        "ranking_date",
    )
    ordering = ("ranking_date",)


admin.site.unregister(Group)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _


from .models import Word, Category, User, Ranking


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "score",
        "is_active",
    )
    search_fields = ("username",)
    ordering = ("username",)

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
                    "score",
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
        "category_word",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
    )
    ordering = ("id",)


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ("id", "ranking_date", "ranking_list")
    readonly_fields = ("ranking_list",)


admin.site.unregister(Group)

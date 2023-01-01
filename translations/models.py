from django.db import models
from django.core.validators import RegexValidator

from users.models import Profile


class Word(models.Model):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected"),
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="word",
    )
    word = models.TextField(
        max_length=255,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z\s']*$",
                message="Word should be alphabetic",
                code="invalid_word",
            )
        ],
    )

    category_word = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "word"]

    def __str__(self):
        return f"{self.word}"


class Translation(models.Model):
    word = models.ForeignKey(
        "Word", on_delete=models.CASCADE, related_name="translations"
    )
    translation = models.CharField(
        max_length=255,
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z\s]*$",
                message="Translation should be alphabetic",
                code="invalid_translation",
            )
        ],
    )
    pronunciation = models.CharField(max_length=100, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.translation


class Category(models.Model):
    users = models.ManyToManyField(Profile, related_name="categories")

    category = models.TextField(max_length=50)
    words = models.ManyToManyField("Word")
    price = models.IntegerField(default=0)
    isDefault = models.BooleanField(default=False)
    isAllow = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category}"

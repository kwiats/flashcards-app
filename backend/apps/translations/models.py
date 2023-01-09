from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from apps.users.models import Profile


class Word(models.Model):
    """Model representing a word

    Fields:
        user (models.ForeignKey):
            Foreign key to the user who created the word.
        word (models.TextField):
            The word itself.
        category_word (models.ForeignKey):
            Foreign key to the category the word belongs to.
        status (models.CharField):
            The status of the word (pending, approved, rejected).
        updated (models.DateTimeField):
            The last time the word was updated.
        created (models.DateTimeField):
            The time the word was created.
    """

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
                regex="^[a-zA-Z\s']*$",  # noqa
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

    def __str__(self) -> str:
        """Return string representation"""
        return self.word


class Translation(models.Model):
    """Model representing a translation of a word.

    Fields::
        word (models.ForeignKey):
            Foreign key to the word being translated.
        translation (models.CharField):
            The translated version of the word.
        pronunciation (models.CharField):
            The pronunciation of the translated word.
        updated (models.DateTimeField):
            The last time the translation was updated.
        created (models.DateTimeField):
            The time the translation was created.
    """

    word = models.ForeignKey(
        "Word", on_delete=models.CASCADE, related_name="translations"
    )
    translation = models.CharField(
        max_length=255,
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z.\s]*$",  # noqa
                message="Translation should be alphabetic",
                code="invalid_translation",
            )
        ],
    )
    pronunciation = models.CharField(max_length=100, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return string representation"""
        return self.translation


class Category(models.Model):
    """Model representing a category of words.

    Fields:
        users (models.ManyToManyField):
            Many-to-many field to the users who have access to this category.
        category (models.TextField):
            The name of the category.
        words (models.ManyToManyField):
            Many-to-many field to the words in this category.
        price (models.IntegerField):
            The price of this category.
        isDefault (models.BooleanField):
            A flag indicating whether this is a default category.
        isAllow (models.BooleanField):
            A flag indicating whether this category is allowed.
    """

    users = models.ManyToManyField(Profile, related_name="categories")

    category = models.TextField(
        max_length=50,
        validators=[
            RegexValidator(
                regex="^[0-9a-zA-Z\s']*$",  # noqa
                message="Word should be alphanumeric",
                code="invalid_title_category",
            )
        ],
    )
    words = models.ManyToManyField("Word")
    price = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Price cannot be less than 0",
            )
        ],
    )
    isDefault = models.BooleanField(default=False)
    isAllow = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Return string representation"""
        return self.category

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, User

from json import dumps


class Ranking(models.Model):
    ranking_date = models.DateTimeField(auto_now=True)
    ranking_name = models.CharField(max_length=50, blank=True)

    @property
    def set_ranking_list(self):
        ranking = dumps(self.actualize_rank())
        return ranking

    def save(self, *args, **kwargs):
        self.ranking = self.set_ranking_list
        super(Ranking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ranking_name}"

    def actualize_rank(self):
        user_list = {}
        user = (
            User.objects.all()
            .order_by("-total_score")
            .values_list("username", flat=True)
        )
        for index, username in enumerate(user):
            user_list[index + 1] = username
        return user_list


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
        "User", on_delete=models.CASCADE, null=True, blank=True, related_name="word"
    )
    word = models.TextField(
        max_length=255,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z]*$",
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

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

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
                regex="^[a-zA-Z]*$",
                message="Translation should be alphabetic",
                code="invalid_translation",
            )
        ],
    )
    pronunciation = models.CharField(max_length=100, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    users = models.ManyToManyField("User", related_name="categories")

    category = models.TextField(max_length=50)
    words = models.ManyToManyField("Word")
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.category}"


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"static/images/user_{instance.pk}/{filename}"


class User(AbstractUser):

    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, unique=True)
    profile_picture = models.FileField(
        upload_to=user_directory_path, null=True, blank=True
    )

    current_score = models.IntegerField(default=0)
    spend_score = models.IntegerField(default=0)
    total_score = models.PositiveIntegerField(db_index=True)

    @property
    def sum_score(self) -> int:
        return self.current_score + self.spend_score

    def save(self, *args, **kwargs):
        self.total_score = self.sum_score
        super(User, self).save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _


class Word(models.Model):

    word = models.TextField(max_length=255)
    translated_word = models.TextField(max_length=255)

    category_word = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        blank=True,
    )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "word"]

    def __str__(self):
        return self.word


class Category(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="categories"
    )

    category = models.TextField(max_length=255)

    words = models.ManyToManyField("Word")

    def __str__(self):
        return self.category


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "static/images/user_{0}/{1}".format(instance.pk, filename)


class User(AbstractUser):

    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, unique=True)

    # own_lists = ...

    profile_picture = models.FileField(
        upload_to=user_directory_path, null=True, blank=True
    )

    score = models.IntegerField(default=0)

from django.db import models
from django.contrib.auth.models import AbstractUser
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

    category = models.TextField(max_length=255)

    words = models.ManyToManyField("Word")

    def __str__(self):
        return self.category


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class CustomUser(AbstractUser):

    profile_picture = models.FileField(
        upload_to=user_directory_path, null=True, blank=True
    )

    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

from django.db import models
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
    WORD_STATUS = (
        ("Wait", "Wait for acceptation"),
        ("Accepted", "Accepted by moderator"),
        ("Unaccepted", "Unaccepted by moderator"),
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=True, blank=True, related_name="word"
    )
    word = models.TextField(max_length=255)
    translated_word = models.TextField(max_length=255)

    category_word = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        blank=True,
    )

    status = models.CharField(max_length=10, choices=WORD_STATUS, default="Wait")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "word"]

    def __str__(self):
        return f"{self.word}"


class Category(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="categories"
    )
    category = models.TextField(max_length=50)
    words = models.ManyToManyField("Word")
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.category}"


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "static/images/user_{0}/{1}".format(instance.pk, filename)


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

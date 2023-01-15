from json import dumps

from apps.users.utills import user_directory_path
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator
from django.db import models


class Profile(AbstractUser):
    """Model representing a user profile.

    Inherits from Django's AbstractUser model.

    Fields:
        profile_picture (models.FileField):
            The profile picture of the user.
        current_score (models.IntegerField):
            The user's current score.
        spend_score (models.IntegerField):
            The user's spend score.
        total_score (models.PositiveIntegerField):
            The user's total score(sum of current and spend score).
    Methods:
        sum_score:
            Return a sum of current score and spend score.
    """

    profile_picture = models.FileField(
        upload_to=user_directory_path, null=True, blank=True
    )

    current_score = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Score cannot be less than 0",
            )
        ],
    )
    spend_score = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Score cannot be less than 0",
            )
        ],
    )
    total_score = models.PositiveIntegerField(db_index=True)

    @property
    def sum_score(self) -> int:
        return self.current_score + self.spend_score

    def save(self, *args, **kwargs):
        self.total_score = self.sum_score
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_username()


class Ranking(models.Model):
    """Model representing a ranking list of users.

    Fields:
        ranking_date (models.DateTimeField):
            The date and time of the ranking.
        ranking_name (models.CharField):
            The name of the ranking.

    Methods:
        actualize_rank:
            Return a dictionary of users and their rankings.
        set_ranking_list:
            Return a JSON representation of the ranking list.
    """

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
        return self.ranking_name

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

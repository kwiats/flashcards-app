from apps.users.utills import user_directory_path
from django.contrib.auth.models import AbstractUser
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

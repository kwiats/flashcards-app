import pytest
from apps.users.models import Profile
from django.core.exceptions import ValidationError

from .factories import ProfileFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestProfileModel:
    @pytest.fixture()
    def profile(self):
        return ProfileFactory.create()

    def test_greater_than_0(self, profile):
        assert profile.spend_score > 0
        assert profile.current_score >= 0

    def test_sum_current_and_spend_score(self, profile):
        assert (
            profile.total_score == profile.spend_score + profile.current_score
        )  # noqa

    def test_spend_score_less_then_0(self, profile):
        with pytest.raises(
            ValidationError,
            match="Score cannot be less than 0",
        ):
            get_field(Profile, "spend_score").run_validators(-1)

    def test_current_score_less_then_0(self, profile):
        with pytest.raises(
            ValidationError,
            match="Score cannot be less than 0",
        ):
            get_field(Profile, "current_score").run_validators(-1)

    def test_profile(self):
        assert get_field(Profile, "name")

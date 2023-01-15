import pytest
from apps.translations.models import Translation
from django.core.exceptions import ValidationError

from .factories import TranslationFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestTranslation:
    def test_translation(self):
        assert get_field(Translation, "word")
        assert get_field(Translation, "translation")
        assert get_field(Translation, "pronunciation")
        assert get_field(Translation, "updated")
        assert get_field(Translation, "created")

    @pytest.fixture()
    def translation(self):
        return TranslationFactory.create()

    def test_string(self, translation):
        assert str(translation) == translation.translation

    def test_translation_user_null_blank(self):
        translation = TranslationFactory.create(user=None)
        assert translation.user is None

    def test_translation_alphabetic(self):
        with pytest.raises(
            ValidationError, match="Translation should be alphabetic"
        ):  # noqa
            get_field(Translation, "translation").run_validators("1dwatrzy3")

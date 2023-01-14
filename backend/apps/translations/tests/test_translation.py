import pytest
from apps.translations.models import Translation

from .factories import TranslationFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestTranslation:
    @pytest.fixture()
    def translation(self):
        return TranslationFactory.create()

    def test_translation(self):
        assert get_field(Translation, "translation")

    def test_string(self, translation):
        assert str(translation) == translation.translation

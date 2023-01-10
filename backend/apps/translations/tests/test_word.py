import pytest
from apps.translations.models import Word

from .factories import WordFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestWord:
    @pytest.fixture()
    def word(self):
        return WordFactory.create()

    def test_word(self):
        assert get_field(Word, "word")

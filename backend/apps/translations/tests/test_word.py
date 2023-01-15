import pytest
from apps.translations.models import Word
from apps.translations.tests.factories import WordFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestWord:
    def test_word(self):
        assert get_field(Word, "user")
        assert get_field(Word, "word")
        assert get_field(Word, "status")
        assert get_field(Word, "updated")
        assert get_field(Word, "created")

    @pytest.fixture()
    def word(self):
        return WordFactory.create()

    def test_string(self, word):
        assert str(word) == word.word

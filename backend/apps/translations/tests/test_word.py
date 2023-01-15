import pytest
from apps.translations.models import Word
from apps.translations.tests.factories import WordFactory
from django.core.exceptions import ValidationError


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

    def test_word_user_null_blank(self):
        word = WordFactory.create(user=None)
        assert word.user is None

    def test_word_validator(self):
        with pytest.raises(ValidationError, match="Word should be alphabetic"):
            get_field(Word, "word").run_validators("1dwa3")

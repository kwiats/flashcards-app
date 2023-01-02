from django.test import TestCase

from users.models import Profile

from .factories import WordFactory


class WordModelTests(TestCase):
    def test_word_user_field(self):
        word = WordFactory()
        self.assertIsInstance(word.user, Profile)

    def test_word_field(self):
        word = WordFactory()
        self.assertIsInstance(word.word, str)

    def test_word_status_field(self):
        word = WordFactory()
        self.assertIn(word.status, ["PENDING", "APPROVED", "REJECTED"])

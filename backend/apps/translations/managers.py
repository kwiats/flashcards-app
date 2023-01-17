# 1. filter by status (approved, pending, rejected)
# 2. filter by user
# 3. filter by word

from django.db import models


class WordManager(models.Manager):
    def filter_by_status(self, status):
        return self.filter(status=status)

    def filter_by_user(self, user):
        return self.filter(user=user)

    def filter_by_word(self, word):
        return self.filter(word=word)

    def filter_by_update(self):
        return self.order_by("updated")

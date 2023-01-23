# 1. filter by status (approved, pending, rejected)
# 2. filter by user
# 3. filter by word

from django.db import models


class WordManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_by_status(self, status):
        return self.get_queryset().filter(status=status)

    def filter_by_user(self, user):
        return self.get_queryset().filter(user=user)

    def filter_by_word(self, word):
        return self.get_queryset().filter(word=word)

    def filter_by_update(self):
        return self.get_queryset().order_by("updated")


class TranslationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_by_update(self):
        return self.get_queryset().order_by("updated")

    def filter_by_created(self):
        return self.get_queryset().order_by("created")

    def filter_by_user(self, user):
        return self.get_queryset().filter(user=user)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isAllow=True)

    def filter_by_default(self):
        return self.get_queryset().filter(isDefault=True)

    def filter_by_low_price(self, price):
        return self.get_queryset().filter(price >= price)

    def filter_by_high_price(self, price):
        return self.get_queryset().filter(price >= price)

    def filter_by_update(self):
        return self.get_queryset().order_by("updated")

    def filter_by_created(self):
        return self.get_queryset().order_by("created")

    def filter_by_user(self, user):
        return self.get_queryset().filter(user=user)

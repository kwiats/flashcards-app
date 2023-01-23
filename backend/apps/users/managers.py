from django.db import models


class ProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_by_spend_score(self, ascending=False):
        if ascending:
            return self.get_queryset().order_by("spend_score")
        return self.get_queryset().order_by("-spend_score")

    def filter_by_current_score(self, ascending=False):
        if ascending:
            return self.get_queryset().order_by("current_score")
        return self.get_queryset().order_by("-current_score")

    def filter_by_total_score(self, ascending=False):
        if ascending:
            return self.get_queryset().order_by("total_score")
        return self.get_queryset().order_by("-total_score")

from django.db import models


class ProfileManager(models.Manager):
    def filter_by_spend_score(self, ascending=False):
        if ascending:
            return self.all().order_by("spend_score")
        return self.all().order_by("-spend_score")

    def filter_by_current_score(self, ascending=False):
        if ascending:
            return self.all().order_by("current_score")
        return self.all().order_by("-current_score")

    def filter_by_total_score(self, ascending=False):
        if ascending:
            return self.all().order_by("total_score")
        return self.all().order_by("-total_score")

from django.db.models.signals import post_save
from django.dispatch import receiver

from .services import generator_word
from .models import Category, User

import re


@receiver(post_save, sender=User)
def create_user_default_list_of_words(sender, instance, **kwargs):
    regex = r"\b{}\b".format("default")
    pattern = re.compile(regex, flags=re.IGNORECASE)
    for obj in Category.objects.all():
        if pattern.search(obj.category):
            return obj.users.add(instance)

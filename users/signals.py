from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from ..translations.models import Category


@receiver(post_save, sender=User)
def create_user_default_list_of_words(sender, instance, **kwargs):
    for obj in Category.objects.all():
        if obj.isDefault:
            return obj.users.add(instance)
        else:
            obj = Category(
                users=instance,
                cateogry="default",
                words=1,
                isAllow=False,
            )
            return obj

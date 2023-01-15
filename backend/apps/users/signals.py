from apps.translations.models import Category
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=Profile)
def create_user_default_list_of_words(sender, instance, created, **kwargs):
    if created:
        default_category = Category.objects.filter(isDefault=True).first()
        print(default_category)
        if default_category:
            default_category.users.add(instance)
        else:
            default_category = Category.objects.create(
                category="default",
                isAllow=False,
                isDefault=True,
            )
            default_category.users.add(instance)

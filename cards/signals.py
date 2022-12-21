from django.db.models.signals import post_save
from django.dispatch import receiver

from .services import generator_word
from .models import Category, User


@receiver(post_save, sender=User)
def create_user_default_list_of_words(sender, instance, **kwargs):
    lst = []
    lst = list(set([word for word in generator_word(amount=1) if len(lst) < 1]))
    category = Category.objects.create(
        user=instance,
        category="Default",
        price=0,
    )
    category.words.set(lst)

from django.db.models.signals import post_save
from django.dispatch import receiver

from .services import generator_word
from .models import Category, User, Word

@receiver(post_save, sender=User)
def create_user_default_list_of_words(sender, instance, **kwargs):
    lst = list(set([word.id for word in generator_word() if len(lst) < 50]))
    print(lst)
    Category.objects.create(user=instance, category="Default", words=lst, price=0)
    
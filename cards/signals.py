from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category, User, Word

@receiver(post_save, sender=User)
def create_user_default_list_of_words(sender, instance, **kwargs):
    # wykonaj akcję po zapisie obiektu MyModel
    pass

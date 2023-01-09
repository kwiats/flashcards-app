import factory
from faker import Faker

from apps.users.models import Profile

fake = Faker("pl_PL")


class ProfileFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("user_name")
    # profile_picture = factory.Faker("file_path", depth=3, category="photo")
    current_score = factory.Faker(
        "random_int",
        min=0,
        max=9999,
    )
    spend_score = factory.Faker(
        "random_int",
        min=0,
        max=9999,
    )
    # total_score = current_score + spend_score

    class Meta:
        model = Profile

from apps.users.models import Profile
from django.contrib.auth.hashers import make_password
from factory import LazyFunction
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import internet, misc

faker = Faker("pl_PL")
faker.add_provider(internet)
faker.add_provider(misc)


class ProfileFactory(DjangoModelFactory):
    # user
    username = faker.user_name()
    password = LazyFunction(lambda: make_password(faker.password()))
    email = faker.email()

    # profile
    profile_picture = faker.file_path(depth=2)
    current_score = faker.random_int(
        min=0,
        max=9999,
    )
    spend_score = faker.random_int(
        min=0,
        max=9999,
    )

    class Meta:
        model = Profile

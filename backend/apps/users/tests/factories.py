from apps.users.models import Profile
from django.contrib.auth.hashers import make_password
from factory import LazyFunction
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import internet, misc

faker = Faker()
faker.add_provider(internet)
faker.add_provider(misc)


class ProfileFactory(DjangoModelFactory):
    # user
    username = LazyFunction(lambda: faker.user_name())
    password = LazyFunction(lambda: make_password(faker.password()))
    email = LazyFunction(lambda: faker.email())
    first_name = LazyFunction(lambda: faker.first_name())
    last_name = LazyFunction(lambda: faker.last_name())
    is_staff = True
    is_superuser = True

    # profile
    profile_picture = LazyFunction(lambda: faker.file_path(depth=2))
    current_score = LazyFunction(
        lambda: faker.random_int(
            min=0,
            max=9999,
        )
    )
    spend_score = LazyFunction(
        lambda: faker.random_int(
            min=0,
            max=9999,
        )
    )

    class Meta:
        model = Profile

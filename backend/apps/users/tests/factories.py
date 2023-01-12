from apps.users.models import Profile
from factory.django import DjangoModelFactory
from faker import Faker

faker = Faker("pl_PL")


class ProfileFactory(DjangoModelFactory):
    name = faker.user_name()
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

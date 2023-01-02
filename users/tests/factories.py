from factory import Factory
from faker import Faker
from users.models import Profile

fake = Faker("en_US")


class ProfileFactory(Factory):
    class Meta:
        model = Profile

    username = fake.name()
    email = fake.email()
    password = fake.password()
    profile_picture = fake.file_path(depth=1)
    current_score = fake.random_int(min=0, max=100)
    spend_score = fake.random_int(min=0, max=100)

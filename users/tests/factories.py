from factory import Factory, Faker

from users.models import Profile


class ProfileFactory(Factory):
    class Meta:
        model = Profile

    username = Faker("name")
    email = Faker("email")
    password = Faker("password")
    profile_picture = Faker("file_path", depth=1)
    current_score = Faker("random_int", min=0, max=100)
    spend_score = Faker("random_int", min=0, max=100)

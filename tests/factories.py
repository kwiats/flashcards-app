import factory

from faker import Faker
from translations.models import Word, Category, Translation
from users.models import User

fake = Faker("pl_PL")


class ProfileFactory(factory.django.DjangoModelFactory):
    name = factory.Faker.name()
    email = factory.Faker.email()
    profile_picture = factory.Faker.file_path(depth=3, category="photo")
    current_score = factory.Faker.random_int(
        min=0,
        max=9999,
    )
    spend_score = factory.Faker.random_int(
        min=0,
        max=9999,
    )
    total_score = current_score + spend_score

    class Meta:
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(ProfileFactory)
    category = factory.Faker.word()
    words = factory.SubFactory("tests.factories.WordFactory", parent=None)
    price = factory.Faker.random_int(
        min=0,
        max=9999,
    )
    isDefault = False
    isAllow = True

    class Meta:
        model = Category


class WordFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(ProfileFactory)
    word = factory.Faker.word()
    category_word = factory.SubFactory(CategoryFactory)
    status = factory.Faker.random_element(
        elements=(
            "PENDING",
            "APPROVED",
            "REJECTED",
        )
    )
    updated = factory.Faker.date_time()
    created = factory.Faker.date_time()

    class Meta:
        model = Word


class TranslationFactory(factory.django.DjangoModelFactory):
    word = factory.SubFactory(WordFactory)
    translation = factory.Faker.text(max_nb_chars=255)
    pronunciation = factory.Faker.word()
    updated = factory.Faker.date_time()
    created = factory.Faker.date_time()

    class Meta:
        model = Translation

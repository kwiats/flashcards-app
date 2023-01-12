from apps.translations.models import Category, Translation, Word
from apps.users.tests.factories import ProfileFactory
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

faker = Faker("pl_PL")


class CategoryFactory(DjangoModelFactory):
    user = SubFactory(ProfileFactory)
    category = faker.word()
    words = SubFactory("tests.factories.WordFactory", parent=None)
    price = faker.random_int(
        min=0,
        max=9999,
    )
    isDefault = False
    isAllow = True

    class Meta:
        model = Category


class WordFactory(DjangoModelFactory):
    user = SubFactory(ProfileFactory)
    word = faker.word()
    category_word = SubFactory(CategoryFactory)
    status = faker.random_element(
        elements=(
            "PENDING",
            "APPROVED",
            "REJECTED",
        ),
    )
    updated = faker.date_time()
    created = faker.date_time()

    class Meta:
        model = Word


class TranslationFactory(DjangoModelFactory):
    word = SubFactory(WordFactory)
    translation = faker.text(max_nb_chars=255)
    pronunciation = faker.word()
    updated = faker.date_time()
    created = faker.date_time()

    class Meta:
        model = Translation

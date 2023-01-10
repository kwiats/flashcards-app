import factory
from apps.translations.models import Category, Translation, Word
from apps.users.tests.factories import ProfileFactory
from faker import Faker

fake = Faker("pl_PL")


class CategoryFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(ProfileFactory)
    category = factory.Faker("word")
    words = factory.SubFactory("tests.factories.WordFactory", parent=None)
    price = factory.Faker(
        "random_int",
        min=0,
        max=9999,
    )
    isDefault = False
    isAllow = True

    class Meta:
        model = Category


class WordFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(ProfileFactory)
    word = factory.Faker("word")
    category_word = factory.SubFactory(CategoryFactory)
    status = factory.Faker(
        "random_element",
        elements=(
            "PENDING",
            "APPROVED",
            "REJECTED",
        ),
    )
    updated = factory.Faker("date_time")
    created = factory.Faker("date_time")

    class Meta:
        model = Word


class TranslationFactory(factory.django.DjangoModelFactory):
    word = factory.SubFactory(WordFactory)
    translation = factory.Faker("text", max_nb_chars=255)
    pronunciation = factory.Faker("word")
    updated = factory.Faker("date_time")
    created = factory.Faker("date_time")

    class Meta:
        model = Translation

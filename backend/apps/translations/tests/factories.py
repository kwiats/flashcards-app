from apps.users.tests.factories import ProfileFactory
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory


class WordFactory(DjangoModelFactory):
    user = SubFactory(ProfileFactory)
    word = Faker("word")
    category_word = SubFactory(
        "apps.translations.tests.factories.CategoryFactory"
    )  # noqa
    status = Faker(
        "random_element",
        elements=("PENDING", "APPROVED", "REJECTED"),
    )
    updated = Faker("date_time")
    created = Faker("date_time")

    class Meta:
        model = "translations.Word"


class TranslationFactory(DjangoModelFactory):
    word = SubFactory(WordFactory)
    translation = Faker("word")
    pronunciation = Faker("word")
    updated = Faker("date_time")
    created = Faker("date_time")

    class Meta:
        model = "translations.Translation"


class CategoryFactory(DjangoModelFactory):
    users = None
    category = Faker("word")
    price = Faker("random_int", min=0, max=1000)
    isDefault = Faker("boolean")

    class Meta:
        model = "translations.Category"

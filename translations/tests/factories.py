from factory import Factory, Faker, SubFactory
from translations.models import Word, Translation, Category

from users.tests.factories import ProfileFactory

faker = Faker()


class WordFactory(Factory):
    class Meta:
        model = Word

    user = SubFactory(ProfileFactory)
    word = Faker("word")
    status = Faker(
        "random_element",
        elements=("PENDING", "APPROVED", "REJECTED"),
    )


class TranslationFactory(Factory):
    class Meta:
        model = Translation

    word = SubFactory(WordFactory)
    translation = Faker("word")
    pronunciation = Faker("word")


class CategoryFactory(Factory):
    class Meta:
        model = Category

    users = SubFactory(ProfileFactory, n=2)
    category = Faker("word")
    words = SubFactory(WordFactory, n=5)
    price = Faker("random_int", min=1, max=1000)
    isDefault = Faker("boolean")
    isAllow = Faker("boolean")

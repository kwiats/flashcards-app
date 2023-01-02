from factory import Factory, SubFactory
from faker import Faker
from translations.models import Word, Translation, Category

from users.tests.factories import ProfileFactory

fake = Faker("en_US")


class WordFactory(Factory):
    class Meta:
        model = Word

    user = SubFactory(ProfileFactory)
    word = fake.word()
    status = fake.random_element(
        elements=("PENDING", "APPROVED", "REJECTED"),
    )


class TranslationFactory(Factory):
    class Meta:
        model = Translation

    word = SubFactory(WordFactory)
    translation = fake.word()
    pronunciation = fake.word()


class CategoryFactory(Factory):
    class Meta:
        model = Category

    users = SubFactory(ProfileFactory, n=2)
    category = fake.word()
    words = SubFactory(WordFactory, n=5)
    price = fake.random_int(min=1, max=1000)
    isDefault = fake.boolean()
    isAllow = fake.boolean()

from apps.users.tests.factories import ProfileFactory
from factory import LazyFunction, RelatedFactory, SubFactory, post_generation
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import internet, misc

faker = Faker()
faker.add_provider(internet)
faker.add_provider(misc)


class WordFactory(DjangoModelFactory):
    user = SubFactory(ProfileFactory)
    word = LazyFunction(lambda: faker.word())
    status = LazyFunction(
        lambda: faker.random_element(
            elements=("PENDING", "APPROVED", "REJECTED"),
        )
    )
    updated = LazyFunction(lambda: faker.date_time())
    created = LazyFunction(lambda: faker.date_time())

    class Meta:
        model = "translations.Word"


class TranslationFactory(DjangoModelFactory):
    word = SubFactory(WordFactory)
    translation = LazyFunction(lambda: faker.word())
    pronunciation = LazyFunction(lambda: faker.word())
    updated = LazyFunction(lambda: faker.date_time())
    created = LazyFunction(lambda: faker.date_time())

    class Meta:
        model = "translations.Translation"


class CategoryFactory(DjangoModelFactory):
    category = LazyFunction(lambda: faker.word())
    price = LazyFunction(lambda: faker.random_int(min=0, max=1000))
    isDefault = LazyFunction(lambda: faker.boolean())

    @post_generation
    def words(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for word in extracted:
                self.words.add(word)

    @post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for user in extracted:
                self.users.add(user)

    class Meta:
        model = "translations.Category"

import factory

from models import Word, Translation, Category


class WordFactory(factory.Factory):
    class Meta:
        model = Word


class TranslationFactory(factory.Factory):
    class Meta:
        model = Translation


class CategoryFactory(factory.Factory):
    class Meta:
        model = Category

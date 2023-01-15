import pytest
from apps.translations.models import Category

from .factories import CategoryFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestCategory:
    def test_category(self):
        assert get_field(Category, "users")
        assert get_field(Category, "category")
        assert get_field(Category, "words")
        assert get_field(Category, "price")
        assert get_field(Category, "isDefault")
        assert get_field(Category, "isAllow")

    @pytest.fixture()
    def category(self):
        return CategoryFactory.create()

    def test_string(self, category):
        assert str(category) == category.category

import pytest
from apps.translations.models import Category

from .factories import CategoryFactory


def get_field(model, field):
    return getattr(model, field).field


@pytest.mark.django_db()
class TestCategory:
    @pytest.fixture()
    def category(self):
        return CategoryFactory.create()

    def test_category(self):
        assert get_field(Category, "category")

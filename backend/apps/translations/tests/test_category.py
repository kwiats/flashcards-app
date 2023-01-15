import pytest
from apps.translations.models import Category
from django.core.exceptions import ValidationError

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
        return CategoryFactory.create(category="Animals")

    def test_string(self, category):
        assert str(category) == category.category

    def test_price_less_then_0(self, category):
        with pytest.raises(
            ValidationError, match="Price cannot be less than 0"
        ):  # noqa
            get_field(Category, "price").run_validators(-1)

    def test_category_name_validator(self):
        with pytest.raises(
            ValidationError, match="Word should be alphanumeric"
        ):  # noqa
            get_field(Category, "category").run_validators("{] [qwe")

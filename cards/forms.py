from django.forms import ModelForm
from .models import Word, Category


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

from apps.translations.models import Category, Translation, Word
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TranslationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = "__all__"

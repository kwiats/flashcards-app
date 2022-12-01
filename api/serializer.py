from cards.models import Word, Category, User
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

from cards.models import Word, Category, User
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"
        write_only = ("id",)
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        write_only = ("id",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

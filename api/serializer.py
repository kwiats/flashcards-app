from cards.models import Word, Category, User, Ranking
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RankingSerializer(serializers.ModelSerializer):
    user_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ranking
        fields = [
            "user_list",
        ]

    def get_user_list(self, data):
        return data.actualize_rank()


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField()
    old_password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password",
        )

    def validate_new_password(self, value):
        validate_password(value)
        return value

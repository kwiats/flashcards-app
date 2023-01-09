from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import Ranking, Profile as User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class ScoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "spend_score",
            "current_score",
            "total_score",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        password = validated_data.get("password", instance.password)
        instance.set_password(password)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance

    def partial_update(self, instance, validated_data):
        instance.update(**validated_data)

        return instance


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

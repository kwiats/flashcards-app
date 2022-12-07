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


class RankingSerializer(serializers.ModelSerializer):
    user_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ranking
        fields = [
            "user_list",
        ]

    def get_user_list(self, data):

        if not hasattr(data, "id"):
            return None
        elif not isinstance(data, Ranking):
            return None
        else:
            return data.actualize_rank()


class ChangePassword(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    oldpassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("oldpassword", "password", "password2")

    def validate(self, atrb):
        if atrb["password"] != atrb["password2"]:
            raise serializers.ValidationError(
                {"password": "Password doesnt match with confirm password."}
            )
        return atrb

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct."}
            )
        return value

    def update(self, instance, validate_data):
        instance.set_password(validate_data["password"])
        instance.save()

        return instance

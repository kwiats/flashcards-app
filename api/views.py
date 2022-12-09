from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins, generics
import pdb


from cards.models import Word, Category, User, Ranking
from .serializer import (
    WordSerializer,
    CategorySerializer,
    UserSerializer,
    RankingSerializer,
    ChangePasswordSerializer,
)


class WordListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordDetailView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = WordSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, raise_exception=True
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):

        word = self.get_object(pk)

        if word:
            serializer = WordSerializer(word, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        serializer = WordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response("Word deleted.", status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        if category:
            serializer = CategorySerializer(category, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            f"Category with id={pk} doesn't exists.", status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request, pk, format=None):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(
            f"Category(id = {pk}) is deleted.", status=status.HTTP_204_NO_CONTENT
        )


class UserListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    print("User detail view")

    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            if user:
                return user
        except:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        if user:
            serializer = UserSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response("User is deleted.", status=status.HTTP_200_OK)


class RankingListView(APIView):
    def get(self, request, format=None):
        ranking = Ranking.objects.latest("ranking_date")
        serializer = RankingSerializer(ranking)
        return Response(serializer.data)


class ChangeEmailView(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            if user:
                return User
        except:
            return None

    def get(self, request):
        return Response("Nothing..")

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")

            if not user.check_password(old_password):
                return Response(
                    ({"old_password": "Wrong password.."}),
                    status=status.HTTP_400_BAD_REQUEST,
                )
            new_password = serializer.data.get("new_password")
            user.set_password(new_password)
            serializer.save()
            return Response(
                "Password is succesfully updated.",
                status=status.HTTP_206_PARTIAL_CONTENT,
            )
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ChangePasswordView(APIView):
    pass

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import pdb


from cards.models import Word, Category, User
from .serializer import WordSerializer, CategorySerializer, UserSerializer


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

        # na dole, nalezy przekazac dane z id == pk
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request, pk, format=None):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

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

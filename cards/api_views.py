from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import User, Word, Category, Answer
from .serializer import (
    AnswerSerializer,
    WordSerializer,
    CategorySerializer,
    UserSerializer,
)


class WordListView(APIView):
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
    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})

    def post(self):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class AnswerView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response({"answers": serializer.data})

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.translations.models import Category, Translation, Word

from . import serializers


class WordListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        words = Word.objects.all()
        serializer = serializers.WordSerializer(words, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordTranslationsView(APIView):
    def get(self, request, pk):
        translations = get_list_or_404(Translation, word=pk)
        word = get_object_or_404(Word, pk=pk)
        serializer = serializers.TranslationSerilizer(translations, many=True)
        return Response({word.word: serializer.data})


class WordDetailView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            word = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return None
        return word

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = serializers.WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        word = self.get_object(pk)

        if word:
            serializer = serializers.WordSerializer(word, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        serializer = serializers.WordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response("Word deleted.", status=status.HTTP_204_NO_CONTENT)


class TranslationListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        translations = get_list_or_404(Translation)
        serializer = serializers.TranslationSerilizer(translations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.TranslationSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TranslationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        obj = get_object_or_404(Translation, pk=pk)
        serializer = serializers.TranslationSerilizer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = get_object_or_404(Translation, pk=pk)
        serializer = serializers.TranslationSerilizer(
            obj,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        obj = get_object_or_404(Translation, pk=pk)
        obj.delete()
        return Response(
            "Translation deleted.",
            status=status.HTTP_204_NO_CONTEN,
        )


class CategoryListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        categories = get_list_or_404(Category)
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None
        return category

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        if category:
            serializer = serializers.CategorySerializer(
                category,
                data=request.data,
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            f"Category with id={pk} doesn't exists.",
            status=status.HTTP_404_NOT_FOUND,
        )

    def post(self, request, pk, format=None):
        serializer = serializers.CategorySerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(
            f"Category(id = {pk}) is deleted.",
            status=status.HTTP_204_NO_CONTENT,
        )

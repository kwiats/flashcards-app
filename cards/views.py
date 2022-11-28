from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm, CategoryForm
from .services import (
    check_translated_word,
    generator_4_options,
    generator_word,
)


def home(request):
    words = Word.objects.all()
    print()
    context = {"words": words}
    return render(request, "cards/home.html", context)


def test(request):

    word = generator_word()
    check_translated_word(word.pk, request.POST.get("dupa", None))

    translated = generator_4_options(word.pk)

    context = {"words": translated, "word": word}
    return render(request, "cards/test.html", context)

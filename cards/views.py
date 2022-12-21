from django.shortcuts import render
from .models import Word
from .services import (
    check_translated_word,
    generator_4_options,
    generator_word,
)


def home(request):
    words = Word.objects.all()
    context = {"words": words}
    return render(request, "cards/home.html", context)


def test(request):

    word = generator_word(amount=1)[0]
    check_translated_word(word.pk, request.POST.get("dupa", None))
    translated = generator_4_options(word.pk)
    context = {"words": translated, "word": word}

    return render(request, "cards/test.html", context)

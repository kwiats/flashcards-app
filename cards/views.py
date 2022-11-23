from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm, CategoryForm
from .services import check_translated_word

# Create your views here.


def home(request):
    words = Word.objects.all()
    print(check_translated_word(1, "Siemano"))
    context = {"words": words}
    return render(request, "cards/home.html", context)

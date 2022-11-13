from django.shortcuts import render, redirect
from .models import Word, Category
from .forms import WordForm, CategoryForm

# Create your views here.


def home(request):
    words = Word.objects.all()
    context = {"words": words}
    return render(request, "cards/home.html", context)


def add_word(request):
    form = WordForm()
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "cards/add_word.html", context)


def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "cards/add_category.html", context)


def flashcards(request):
    words = Word.objects.all()
    q = request.POST.get("q")
    print(q)
    context = {"words": words}
    return render(request, "cards/flashcards.html", context)

from django.shortcuts import render, redirect
from .models import Word, Category
from .forms import WordForm, CategoryForm
from .services import Learning

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


ids = Word.objects.values_list("id", flat=True)
learn = Learning(100, ids)
rnd_list = learn.gen_list_of_words()


def flashcards(request):
    word = Word.objects.get(id=learn.get_random_id())

    q = request.POST.get("q")
    print(q)
    context = {"words": word}
    return render(request, "cards/flashcards.html", context)

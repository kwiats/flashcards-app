from random import choice
from django.shortcuts import get_object_or_404


from .models import Word, User, Category


def generator_word(amount: int) -> list:
    lst = []
    for _ in range(amount):
        lst.append(choice(Word.objects.all()))
    return lst


def generator_4_options(pk):
    lst = []
    while len(lst) != 3:
        word = choice(Word.objects.all())
        if word.pk != pk:
            lst.append(word)

    main_word = Word.objects.get(pk=pk)
    lst.append(main_word)
    return lst


def check_translated_word(pk, user_answer):
    result = False
    if user_answer:
        word = get_object_or_404(Word, pk=pk)
        translated_word = word.translated_word
        if translated_word == user_answer:
            result = True
    return result


def buy_category(user, category_id) -> bool:
    category = get_object_or_404(Category, pk=category_id)
    result = False
    if user.current_score >= category.price:
        substract_user_score(user=user, score=category.price)
        category.users.add(user.username)
        category.update()
        result = True
    return result


def substract_user_score(user, score) -> User:
    user.current_score -= score
    user.spend_score += score
    user.update()
    return user

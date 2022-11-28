from random import choice

from .models import Word, User


def add_points_for_user(pk):
    user_instance = User.objects.get(pk=pk)
    user_instance.score += 4
    score = user_instance.score
    user_instance.save()
    return score


def generator_word():
    return choice(Word.objects.all())


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
    if user_answer:
        word = Word.objects.get(pk=pk)
        translated_word = word.translated_word
        print(translated_word)
        print(user_answer)
        if translated_word == user_answer:
            add_points_for_user(pk)
        return None

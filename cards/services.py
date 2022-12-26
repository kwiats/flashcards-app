from random import choice

from .models import Word, User, Category


def add_points_for_user(pk):
    user_instance = User.objects.get(pk=pk)
    user_instance.current_score += 4
    score = user_instance.current_score
    user_instance.save()
    return score


def minus_point_for_user(pk):
    user_instance = User.objects.get(pk=pk)
    user_instance.current_score -= 1
    score = user_instance.current_score
    user_instance.save()
    return score


def check_score_to_buy(
    category_id,
    user_id,
):
    current_score = User.objects.get(pk=user_id).current_score
    category_price = Category.objects.get(pk=category_id).price
    if (current_score - category_price) > 0:
        return True
    return False


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
    if user_answer:
        word = Word.objects.get(pk=pk)
        translated_word = word.translated_word
        print(translated_word)
        print(user_answer)
        if translated_word == user_answer:
            return add_points_for_user(pk)
        return minus_point_for_user(pk)
    return None


def buy_category(user_id, category_id) -> bool:
    category = Category.objects.get(pk=category_id)
    user = User.objects.get(pk=user_id)
    if user.current_score > category.price:
        substract_user_score(user_id=user_id, score=category.price)
        return True
    return False


def substract_user_score(user_id, score) -> User:
    user = User.objects.get(pk=user_id)
    user.current_score -= score
    user.spend_score += score
    return user

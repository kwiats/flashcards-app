from random import choice
from django.shortcuts import get_object_or_404


from .models import Word, User, Category


def generator_word(amount: int) -> list:
    """
    Generates a list of 'amount' Word objects chosen randomly from the Word model.

    Parameters:
        amount (int): The number of Word objects to generate.

    Returns:
        list: A list of 'amount' Word objects.
    """
    lst = []
    for _ in range(amount):
        lst.append(choice(Word.objects.all()))
    return lst


def generator_4_options(pk: int) -> list:
    """
    Generates a list of 4 Word objects, including the Word object with primary key 'pk'.
    The other 3 Word objects are chosen randomly from the Word model and are different from the Word object with primary key 'pk'.

    Parameters:
        pk (int): The primary key of the Word object to include in the generated list.

    Returns:
        list: A list of 4 Word objects, including the Word object with primary key 'pk'.
    """
    lst = []
    while len(lst) != 3:
        word = choice(Word.objects.all())
        if word.pk != pk:
            lst.append(word)

    main_word = Word.objects.get(pk=pk)
    lst.append(main_word)
    return lst


def check_translated_word(pk: int, user_answer: str) -> bool:
    """
    Checks if the user's answer matches the translated word of the Word object with primary key 'pk'.

    Parameters:
        pk (int): The primary key of the Word object to check.
        user_answer (str): The user's answer to check against the translated word.

    Returns:
        bool: True if the user's answer matches the translated word, False otherwise.
    """
    result = False
    if user_answer:
        word = get_object_or_404(Word, pk=pk)
        translated_word = word.translated_word
        if translated_word == user_answer:
            result = True
    return result


def buy_category(user: User, category_id: int) -> bool:
    """Allow a user to buy a category if they have enough current score.

    Parameters:
    user (User): The user object.
    category_id (int): The ID of the category to be purchased.

    Returns:
    bool: True if the purchase was successful, False otherwise.
    """
    category = get_object_or_404(Category, pk=category_id)
    result = False
    if user.current_score >= category.price:
        update_user_score(user=user, score=category.price)
        category.users.add(user.username)
        category.update()
        result = True
    return result


def update_user_score(user: User, score: int) -> User:
    """Update a user's current score and spend score by substracting a given score.

    Parameters:
    user (User): The user object.
    score (int): The score to be substracted from the user's current score.

    Returns:
    User: The updated user object.
    """
    user.current_score -= score
    user.spend_score += score
    user.update()
    return user

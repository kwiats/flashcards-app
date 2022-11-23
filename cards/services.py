from .models import Word


def check_translated_word(pk, user_answer):
    word = Word.objects.get(pk=pk)
    translated_word = word.translated_word
    if translated_word == user_answer:
        return f"{translated_word} -> {user_answer} OK"
    return f"{translated_word} -> {user_answer} ERROR"

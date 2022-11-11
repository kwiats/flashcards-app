from django.db import models


class Word(models.Model):

    word = models.TextField(max_length=255)
    translated_word = models.TextField(max_length=255)

    category_word = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
        blank=True,
    )

    updated = models.DateTimeField(auto_now_=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


class Category(models.Model):

    category = models.TextField(max_length=255)

    words = models.ManyToManyField("Word")

    def __str__(self):
        return self.category

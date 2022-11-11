from django.db import models

class Word(models.Model):

    word = models.TextField(max_length=255)
    translated_word = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.word} -> {self.translated_word}"
    
class Category(models.Model):

    category = models.TextField(max_length=255)

    words = models.ManyToManyField('Word')

    def __str__(self):
        return self.category

from django.contrib import admin
from .models import Word, Category, Answer, User

# Register your models here.
admin.site.register(Word)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(User)

# Generated by Django 4.1.3 on 2023-01-15 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("translations", "0003_alter_category_category_alter_category_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="word",
            name="category_word",
        ),
    ]

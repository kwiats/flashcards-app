# Generated by Django 4.1.3 on 2022-11-11 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_word_category_word_word_created_word_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="word",
            name="category_word",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="cards.category",
            ),
        ),
        migrations.AlterField(
            model_name="word",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="word",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
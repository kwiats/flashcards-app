# Generated by Django 4.1.3 on 2023-01-22 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("translations", "0005_translation_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
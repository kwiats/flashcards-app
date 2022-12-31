# Generated by Django 4.1.3 on 2022-12-19 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0004_alter_word_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ranking",
            name="ranking_list",
        ),
        migrations.AddField(
            model_name="ranking",
            name="ranking_name",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="category",
            name="category",
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name="word",
            name="status",
            field=models.CharField(
                choices=[
                    ("Wait", "Wait for acceptation"),
                    ("Accepted", "Accepted by moderator"),
                    ("Unaccepted", "Unaccepted by moderator"),
                ],
                default="Wait",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="word",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="word",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

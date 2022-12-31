# Generated by Django 4.1.3 on 2022-12-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_category_price_word_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="word",
            name="status",
            field=models.CharField(
                choices=[
                    ("Wait", "Wait for aceptation"),
                    ("Accepted", "Accepted by moderator"),
                    ("Unaccepted", "Unaccepted by moderator"),
                ],
                default="Wait",
                max_length=10,
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0007_alter_ranking_ranking_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ranking",
            name="ranking_list",
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 4.1.3 on 2023-01-22 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_profile_name_alter_profile_current_score_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Ranking",
        ),
        migrations.AlterModelManagers(
            name="profile",
            managers=[],
        ),
    ]
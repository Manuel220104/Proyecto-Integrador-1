# Generated by Django 4.2.4 on 2023-08-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Books", "0003_alter_book_editorial_alter_book_language_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="Like",
        ),
        migrations.AddField(
            model_name="book",
            name="Authors",
            field=models.CharField(default="Autor", max_length=200),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Technologys', '0004_technology_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='Name',
            field=models.CharField(max_length=60),
        ),
    ]

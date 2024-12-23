# Generated by Django 5.1.3 on 2024-12-05 20:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_alter_book_imagelink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2024)]),
        ),
    ]

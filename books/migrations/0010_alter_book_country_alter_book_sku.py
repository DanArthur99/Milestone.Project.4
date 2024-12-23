# Generated by Django 5.1.3 on 2024-11-27 00:12

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_review_title_alter_review_book_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]

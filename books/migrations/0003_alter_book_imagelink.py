# Generated by Django 5.1.3 on 2024-11-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_title_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='imageLink',
            field=models.ImageField(blank=True, max_length=1024, null=True, upload_to=''),
        ),
    ]

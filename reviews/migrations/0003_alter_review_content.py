# Generated by Django 5.1.3 on 2024-11-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_review_book_id_remove_review_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
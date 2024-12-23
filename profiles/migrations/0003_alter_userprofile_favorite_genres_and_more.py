# Generated by Django 5.1.3 on 2024-11-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_rating'),
        ('profiles', '0002_userprofile_favorite_genres_userprofile_reading_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_who_like_this_genre', to='books.genre'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='reading_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_who_are_interested_in_this_book', to='books.book'),
        ),
    ]

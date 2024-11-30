# Generated by Django 5.1.3 on 2024-11-30 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_favorite_genres_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_postcode',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='town_or_city',
        ),
    ]
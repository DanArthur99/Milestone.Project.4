from django.db import models
import profiles
import datetime
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
# Create your models here.


class Genre(models.Model):
    "Genre model"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    """Book model"""
    author = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    language = models.CharField(max_length=254)
    pages = models.PositiveIntegerField()
    year = models.IntegerField(
        validators=[MaxValueValidator(datetime.date.today().year)])
    country = CountryField(blank_label='Country', null=True, blank=True)
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)], null=True, blank=True)
    genres = models.ManyToManyField(
            Genre, related_name="books_with_this_genre")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    imageLink = CloudinaryField(
            'image', blank=True, null=True, help_text="Book Image")

    def __str__(self):
        return self.name

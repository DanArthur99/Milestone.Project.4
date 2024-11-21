from django.db import models

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    author =  models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    book_code = models.CharField(max_length=254, null=True, blank=True)
    language = models.CharField(max_length=254)
    pages = models.IntegerField()
    year = models.IntegerField()
    country = models.CharField(max_length=254)
    genres = models.ManyToManyField(Genre, related_name="books_with_this_genre")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    imageLink = models.ImageField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import books
import profiles
# Create your models here.


class Review(models.Model):
    """Review model"""
    book = models.ForeignKey(
        'books.Book', null=True, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        'profiles.UserProfile',
        null=True, blank=False,
        on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=True, blank=False)
    user_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], null=True,
        blank=False)
    content = models.TextField(max_length=1000, null=True, blank=True)

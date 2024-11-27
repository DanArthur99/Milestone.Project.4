from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import books
import profiles
# Create your models here.

class Review(models.Model):
    book_id = models.ForeignKey('books.Book', null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey('profiles.UserProfile', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=True, blank=False)
    user_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False, blank=False)
    content = models.CharField(max_length=1000, null=True, blank=True)
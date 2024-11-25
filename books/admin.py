from django.contrib import admin
from .models import Book, Genre, Review

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    filter_horizontal = ('genres',)

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review)


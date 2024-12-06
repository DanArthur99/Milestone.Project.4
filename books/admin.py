from django.contrib import admin
from .models import Book, Genre

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    """Adds book data to the admin page"""
    filter_horizontal = ('genres',)

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)


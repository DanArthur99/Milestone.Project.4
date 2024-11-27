from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:book_id>/', views.about_book, name='about_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),
]
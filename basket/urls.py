from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<book_id>/', views.add_to_basket, name='add_to_basket'),
    path('amend/<book_id>/', views.adjust_basket, name='adjust_basket'),
    path('remove/<book_id>/', views.remove_from_basket, name='remove_from_basket'),
]
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def basket_contents(request):

    basket_items = []
    total = 0
    book_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        book = get_object_or_404(Book, pk=item_id)
        total += quantity * book.price
        book_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })
       

    context = {
        'basket_items': basket_items,
        'total': total,
        'book_count': book_count,
    }

    return context
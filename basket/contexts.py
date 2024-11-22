from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book


def basket_contents(request):

    basket_items = []
    total = 0
    book_count = 0
    basket = request.session.get('basket', {})

    for book_id, book_data in basket.items():
        if isinstance(book_data, int):
            book = get_object_or_404(Book, pk=book_id)
            total += book_data * book.price
            book_count += book_data
            basket_items.append({
                'book_id': book_id,
                'quantity': book_data,
                'book': book,
            })
        else:
            book = get_object_or_404(Book, pk=book_id)
            for quantity in book_data.items():
                total += quantity * book.price
                book_count += quantity
                basket_items.append({
                    'book_id': book_id,
                    'quantity': quantity,
                    'book': book,
                })


    context = {
        'basket_items': basket_items,
        'total': total,
        'book_count': book_count,
        'total': total,
    }

    return context
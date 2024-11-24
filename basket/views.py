from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404
)
from django.urls import reverse
from django.contrib import messages

from books.models import Book


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, book_id):
    """ Add a quantity of the specified book to the shopping basket """

    book = get_object_or_404(Book, pk=book_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})


    if book_id in list(basket.keys()):
        basket[book_id] += quantity
        messages.success(request,
                        (f'Updated {book.name} '
                        f'quantity to {basket[book_id]}'))
    else:
        basket[book_id] = quantity
        messages.success(request, f'Added {book.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, book_id):
    """Adjust the quantity of the specified book to the specified amount"""

    book = get_object_or_404(Book, pk=book_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    
    if quantity > 0:
        basket[book_id] = quantity
        messages.success(request,
                        (f'Updated {book.name} '
                        f'quantity to {basket[book_id]}'))
    else:
        basket.pop(book_id)
        messages.success(request,
                        (f'Removed {book.name} '
                        f'from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, book_id):
    """Remove the book from the shopping basket"""

    try:
        book = get_object_or_404(Book, pk=book_id)
        basket = request.session.get('basket', {})

        basket.pop(book_id)
        messages.success(request, f'Removed {book.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing book: {e}')
        return HttpResponse(status=500)

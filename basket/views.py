from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404
)
from django.urls import reverse
from django.contrib import messages

from books.models import Book


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified book to the shopping basket """

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})


    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                        (f'Updated {book.name} '
                        f'quantity to {basket[item_id]}'))
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {book.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified book to the specified amount"""

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'book_size' in request.POST:
        size = request.POST['book_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{book.name} quantity to '
                              f'{basket[item_id]["items_by_size"][size]}'))
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{book.name} from your basket'))
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request,
                             (f'Updated {book.name} '
                              f'quantity to {basket[item_id]}'))
        else:
            basket.pop(item_id)
            messages.success(request,
                             (f'Removed {book.name} '
                              f'from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        book = get_object_or_404(Book, pk=item_id)
        size = None
        if 'book_size' in request.POST:
            size = request.POST['book_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{book.name} from your basket'))
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {book.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

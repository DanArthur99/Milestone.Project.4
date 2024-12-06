from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Book, Genre
from reviews.models import Review
from .forms import BookForm
# Create your views here.

def all_books(request):
    """ A view to show all books, including sorting and search queries """

    books = Book.objects.all()
    reviews = Review.objects
    query = None
    genres = None
    sort = None
    direction = None

    for book in books:
        new_rating = 0
        reviews = Review.objects.filter(book=book)
        if reviews:
            for review in reviews:
                new_rating += review.user_rating    
            book.rating = new_rating / len(reviews)
            book.save()
        else:
            book.rating = None
            book.save()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

        if 'genres' in request.GET:
            genres = request.GET['genres'].split(',')
            books = books.filter(genres__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('books'))

            queries = Q(name__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
    }

    return render(request, 'books/books.html', context)

def about_book(request, book_id):
    """ A view to show individual book details """

    book = get_object_or_404(Book, pk=book_id)

    new_rating = 0
    reviews = Review.objects.filter(book=book)
    if reviews:
        for review in reviews:
            new_rating += review.user_rating    
        book.rating = new_rating / len(reviews)
        book.save()
    
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            reviews = reviews.order_by(sortkey)
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            reviews = reviews.order_by(sortkey)

    current_sorting = f'{sort}-{direction}'

    context = {
        'book': book,
        'reviews': reviews,
        'current_sorting': current_sorting,
        'user': request.user
    }

    return render(request, 'books/about_book.html', context)

@login_required
def add_book(request):
    """ Add a book to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('about_book', args=[book.id]))
        else:
            messages.error(request,
                           ('Failed to add book. '
                            'Please ensure the form is valid.'))
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_book(request, book_id):
    """ Edit a book in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('homepage'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('about_book', args=[book.id]))
        else:
            messages.error(request,
                           ('Failed to update book. '
                            'Please ensure the form is valid.'))
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.name}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def delete_book(request, book_id):
    """ Delete a book from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        messages.success(request, 'Book deleted!')
        return redirect(reverse('books'))
    
    template = 'books/delete_book.html'
    context = {
        'book': book
    }
    return render(request, template, context)

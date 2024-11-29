from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile
from books.models import Book

# Create your views here.

@login_required
def add_review(request, book_id):

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        userprofile = get_object_or_404(UserProfile, user=request.user)
        book = get_object_or_404(Book, pk=book_id)
        if form.is_valid():  
            form.instance.user = userprofile
            form.instance.book = book
            review = form.save()
            all_reviews = Review.objects.filter(book=book)
            book_rating = 0
            for rev in all_reviews:
                book_rating += rev.user_rating
            book.rating = book_rating / len(all_reviews)
            book.save()
            return redirect(reverse('about_book', args=[book_id]))
        else:
            messages.error(request,
                           ('Failed to add review. '
                            'Please ensure the form is valid.'))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'book_id': book_id,
        'form': form,
    }

    return render(request, template, context)
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
    """Add a review"""
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

@login_required
def edit_review(request, review_id):
    """Edit a review"""
    review = get_object_or_404(Review, pk=review_id)
    book = review.book
    book_id = book.id

    if not request.user.is_superuser and request.user != review.user :
        messages.error(request, "Oops, looks like this page's access is forbidden")
        return redirect(reverse('homepage'))
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():  
            form.save()
            messages.success(request, 'Successfully updated review!')
            # Updates average rating
            return redirect(reverse('about_book', args=[book_id]))
        else:
            messages.error(request,
                           ('Failed to add review. '
                            'Please ensure the form is valid.'))
    else:
        form =  ReviewForm(instance=review)
        messages.info(request, f'You are editing a review for {book.name}')

    template = 'reviews/edit_review.html'
    context = {
        'book_id': book_id,
        'review_id': review_id,
        'form': form,
    }

    return render(request, template, context)

@login_required
def delete_review(request, review_id):
    """ Delete a review from the about book page """
    review = get_object_or_404(Review, pk=review_id)
    book = review.book

    if not request.user.is_superuser and request.user != review.user :
        messages.error(request, "Oops, looks like this functionality is forbidden")
        return redirect(reverse('homepage'))
    if request.method == "POST": 
        review.delete()
        messages.success(request, 'Review deleted!')
        return redirect(reverse('about_book', args=[book.id]))
    
    template = "reviews/delete_review.html"
    context = {
        "book": book,
        "review": review
    }
    return render(request, template, context)
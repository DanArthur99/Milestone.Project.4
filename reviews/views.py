from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Review
from .forms import ReviewForm

# Create your views here.

@login_required
def add_review(request, book_id):

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            review.book_id = book_id
            review.user_id = request.user.id
            messages.success(request, 'Successfully added review')
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
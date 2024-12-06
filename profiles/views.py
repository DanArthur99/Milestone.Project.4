from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.urls import reverse

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """Displays order history on user profile page"""
    order = get_object_or_404(Order, order_number=order_number)

    if (
        not request.user.is_superuser) and (
            order.user_profile.user != request.user):
        messages.error(
            request,
            "Unauthorized Access")
        return redirect(reverse('homepage'))

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

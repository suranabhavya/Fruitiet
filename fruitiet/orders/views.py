import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from carts.models import Cart
from .models import Order
from .utils import id_generator
# Create your views here.

def orders(request):
    context = {}
    template = "orders/user.html"
    return render(request, template, context)

# require user login
@login_required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        # Work on some error message
        return HttpResponseRedirect(reverse("cart"))

    # assign address
    # run credit card
    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))

    context = {}
    template = "products/home.html"
    return render(request, template, context)
from django.urls import path

from . import views

urlpatterns = [
    path("cart", views.view, name="cart"),
    path("cart/<slug:slug>", views.update_cart, name="update_cart"),
]
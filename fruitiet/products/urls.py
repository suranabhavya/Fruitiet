from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("store", views.store, name="store"),
    path("store/<slug:slug>", views.single, name="single_product"),
    path("search/", views.search, name="search")
]
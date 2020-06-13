from django.urls import path

from . import views

urlpatterns = [
    path("accounts/logout", views.logout_view, name="auth_logout"),
    path("accounts/login/", views.login_view, name="auth_login"),
    path("accounts/register", views.registration_view, name="auth_register"),
]
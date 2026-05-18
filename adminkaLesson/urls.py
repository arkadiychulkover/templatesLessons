from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

urlpatterns = [
    path("signup/", views.register_page, name="register_page"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_view, name="logout_view"),
    path("auth/", views.auth_page, name="auth_page"),
    path("newuser/", views.register_view, name="register_view"),
    path("login-view/", views.login_view, name="login_view"),
]
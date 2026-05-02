from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("simple_form/", views.postuser, name="simple_form"),
    path("postuser/", views.postuser, name="about"),
    path("user/", views.user_form, name="user_form"),
    path("seller/", views.seller_form, name="seller_form"),
    path("product/", views.product_form, name="product_form"),
    path("sales/", views.sales_form, name="sales_form"),
]
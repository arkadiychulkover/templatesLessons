from django.urls import path
from . import views

urlpatterns = [
    path("text/", views.text_format, name="text_format"),
    path("contacts/", views.contacts, name="contacts"),
    path("style/", views.style, name="style"),
    path("products/", views.products, name="products"),
    path('time/', views.time, name='time'),
]
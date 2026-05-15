from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

urlpatterns = [
    # path("", views.seed, name="index"),
    # path("/pint", views.get_all_products, name="print")
    # path('', views.contact_list, name='contact_list'),
    # path('add/', views.add_contact, name='add_contact'),
    # path('', views.product_list, name="product_list"),
    # path('addprod/', views.create_product, name='create_product'),
    # path('delete/<str:pk>/', views.delete_product, name='delete_product'),
    # path('update/', views.update_product, name='update_product'),
    path('seed/', views.seed_lib),
    path('books/', views.all_books),
    path('readers/', views.all_readers),
    path('books/available/', views.available_books),
    path('readers/<int:pk>/books/', views.reader_books),
]
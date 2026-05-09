from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

urlpatterns = [
    # path("", views.seed, name="index"),
    # path("/pint", views.get_all_products, name="print")
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
]
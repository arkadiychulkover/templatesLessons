from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

urlpatterns = [
    path('customers/', views.customers_list),
    path('sellers/', views.sellers_list),
    path('products/', views.products_list),
    path('sales/', views.sales_list),

    path('addcustomers/', views.customer_view),
    path('addsellers/', views.seller_view),
    path('addsales/', views.sale_view),
]
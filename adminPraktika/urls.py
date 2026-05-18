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

    path('deletecustomer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('deleteseller/<int:pk>/', views.delete_seller, name='delete_seller'),
    path('deletesale/<int:pk>/', views.delete_sale, name='delete_sale'),    
    path('deleteproduct/<int:pk>/', views.delete_product, name='delete_product'),
]
from django.contrib import admin
from .models import Product, Sale, Seller, Customer

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Sale)
admin.site.register(Product)
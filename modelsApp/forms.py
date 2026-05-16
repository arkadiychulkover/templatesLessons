from django import forms
from .models import Contact, Customer, Product, Sale, Seller


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'number', 'notes']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']









class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'email', 'phone', 'hire_date', 'position']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'seller', 'product', 'sale_date', 'amount']    
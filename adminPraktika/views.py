from django.shortcuts import render
from .models import Customer, Product, Seller, Sale
from .forms import CustomerForm, ProductForm, SaleForm, SellerForm
from django.views import View
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

def customers_list(request):
    data = list(Customer.objects.values(
        'id',
        'first_name',
        'last_name',
        'email',
        'phone'
    ))
    return JsonResponse(data, safe=False)


def sellers_list(request):
    data = list(Seller.objects.values(
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'hire_date',
        'position'
    ))
    return JsonResponse(data, safe=False)


def products_list(request):
    data = list(Product.objects.values(
        'id',
        'name',
        'price',
        'description',
        'created_at',
        'updated_at'
    ))
    return JsonResponse(data, safe=False)


def sales_list(request):
    data = list(Sale.objects.select_related(
        'customer', 'seller', 'product'
    ).values(
        'id',
        'sale_date',
        'amount',
        'customer__first_name',
        'customer__last_name',
        'seller__first_name',
        'seller__last_name',
        'product__name'
    ))
    return JsonResponse(data, safe=False)










def product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Product created successfully"}, status=201)

    else:
        form = ProductForm()

    return render(request, "defoult_form.html", {'form': form})

def sale_view(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Sale created successfully"}, status=201)

    else:
        form = SaleForm()

    return render(request, "defoult_form.html", {'form': form})

def seller_view(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Seller created successfully"}, status=201)

    else:
        form = SellerForm()

    return render(request, "defoult_form.html", {'form': form})

def customer_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Customer created successfully"}, status=201)

    else:
        form = CustomerForm()

    return render(request, "defoult_form.html", {'form': form})





@csrf_exempt
def delete_product(request, pk):
    try:        
        if request.method == 'DELETE':
            Product.objects.filter(id=pk).delete()
            return JsonResponse({"status": "OK"}, status=200)
        return JsonResponse({"error": "Method not allowed"}, status=405)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt
def delete_sale(request, pk):
    try:        
        if request.method == 'DELETE':
            Sale.objects.filter(id=pk).delete()
            return JsonResponse({"status": "OK"}, status=200)
        return JsonResponse({"error": "Method not allowed"}, status=405)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt
def delete_seller(request, pk):
    try:        
        if request.method == 'DELETE':
            Seller.objects.filter(id=pk).delete()
            return JsonResponse({"status": "OK"}, status=200)
        return JsonResponse({"error": "Method not allowed"}, status=405)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt
def delete_customer(request, pk):
    try:        
        if request.method == 'DELETE':
            Customer.objects.filter(id=pk).delete()
            return JsonResponse({"status": "OK"}, status=200)
        return JsonResponse({"error": "Method not allowed"}, status=405)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
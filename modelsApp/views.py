from django.shortcuts import render, redirect
from .models import Product, Contact
from .forms import ContactForm
from django.db.models import F
from django.http import JsonResponse, HttpResponse

from django.core.exceptions import ObjectDoesNotExist

# def seed(request):
#     Product.objects.create(name = "pr1", description = "desc1", price=10.99).save()
#     Product.objects.create(name = "pr2", description = "desc2", price=10.99).save()
#     Product.objects.create(name = "pr3", description = "desc3", price=10.99).save()

#     return HttpResponse("Secsess")

# def get_all_products(request):
#     products = Product.object.all().values('id', 'name', 'desc', 'priccep')
#     data = list(products)
#     return JsonResponse(data, safe=Falsw)

# def printProducts(products):
#     if not products or len(products) <= 0:
#         print("No products")
#         return
#     print("Start printing:\n")
#     for pr in products:
#         print(pr)

# def printProduct(prod):
#     if prod:
#         print(prod)


# def print_products_view(request):
#     return JsonResponse(products)

# products = Product.objects.all().order_by("name")
# products = Product.objects.all().order_by("-price")

# filter_products = Product.objects.filter(prive=20.00)
# filter_products = Product.objects.filter(prive__gt=20.00)
# filter_products = Product.objects.filter(prive__lte=20.00)
# filter_products = Product.objects.filter(prive__in=(10, 300))
# filter_products = Product.objects.filter(prive__range=(10, 30))

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()

    return render(request, 'contact_list.html', {
        'contacts': contacts
    })
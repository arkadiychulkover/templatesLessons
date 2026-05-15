from django.shortcuts import render, redirect
from .models import Product, Contact, Project, Reader, Task, Book
from .forms import ContactForm, ProductForm, ProductUpdateForm
from django.db.models import F
from django.views import View
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators import method_decorator
 

from django.core.exceptions import ObjectDoesNotExist

# def seed(request):
#     Product.objects.create(name = "pr1", description = "desc1", price=10.99).save()
#     Product.objects.create(name = "pr2", description = "desc2", price=10.99).save()
#     Product.objects.create(name = "pr3", description = "desc3", price=10.99).save()

#     return HttpResponse("Secsess")

# def get_all_products(request):
#     products = Product.object.all().values('id', 'name', 'desc', 'priccep')
#     data = list(products)
#     return JsonResponse(data, safe=False)

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


# # def print_products_view(request):
# #     return JsonResponse(products)

# # products = Product.objects.all().order_by("name")
# # products = Product.objects.all().order_by("-price")

# # filter_products = Product.objects.filter(price=20.00)
# # filter_products = Product.objects.filter(price__gt=20.00)
# # filter_products = Product.objects.filter(price__lte=20.00)
# # filter_products = Product.objects.filter(price__in=(10, 300))
# # filter_products = Product.objects.filter(price__range=(10, 30))
# # filter_products = Product.objects.filter(name__exact="Name1")
# # filter_products = Product.objects.filter(name__exact="duct")
# # filter_products = Product.objects.filter(name__isstartswith="Pro")
# # filter_products = Product.objects.filter(name__iendwith="ct 1") & filter_products = Product.objects.filter(name__isstartswith="Pro")

# # try:
# #     profuct = Product.objects.get(id="example")
# #     profuct2 = Product.objects.filter(id="example").update(name = "name", price = F("price")+10)
# #     print(product)

# # except ObjectDoesNotExist:
# #     print("no product with this id")


# def product_list(request):
#     prod = Product.objects.all()
#     return render(request, "product_list.html", {"products":prod})

# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("product_list")
#     else:
#         form = ProductForm()

#     return render(request, "add_product.html", {'form': form})

# @csrf_exempt
# def delete_product(request, pk):
#     try:        
#         if request.method == 'DELETE':
#             Product.objects.filter(id=pk).delete()
#             return JsonResponse({"status": "OK"}, status=200)
#         return JsonResponse({"error": "Method not allowed"}, status=405)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# def update_product(request):
#     if request.method == 'POST':
#         form = ProductUpdateForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             description = form.cleaned_data["description"]
#             price = form.cleaned_data["price"]

#             Product.objects.filter(name=name).update(name=name, description=description, price=price)
#             return redirect("product_list")

#     else:
#         form = ProductUpdateForm()

#     return render(request, "update_product.html", {'form': form})
      

# @method_decorator(csrf_exempt, name="dispatch")
# class ProjectListView(View):
#     def get(self, request):
#         projects = Project.objects.all().values('id', 'name', 'description')
#         data = list(projects)
#         return JsonResponse(data, safe=False)
    
#     def post(self, request):
#         try:
#             payload = json.loads(request.body)
#             if not payload.get('name') or not payload.get('description'):
#                 return JsonResponse({'error': 'Name and description are required'}, status=400)
#             project = Project.objects.create(
#                 name=payload.get('name'),
#                 description=payload.get('description')
#             )
#             return JsonResponse({'id': str(project.id), 'message': 'Project created successfully'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)


# @method_decorator(csrf_exempt, name='dispatcch')
# class ProjectDetailView(View):
#     def get(self, request, pk):
#         try:
#             project = Project.objects.prefetch_related("task").get(id=pk)
#             data = {
#                 'id': str(project.id),
#                 'name': project.name,
#                 'description': project.description,
#                 'progress': project.get_progress(),
#             }
#             return JsonResponse(data)
#         except ObjectDoesNotExist:
#             return JsonResponse({'error': 'Project not found'}, status=404)

# def post(self, request, pk):
#     try:
#         project = Project.objects.prefetch_related("tasks").get(id=pk)
#         payload = json.loads(request.body)
#         project.tasks.create(
#             name=payload.get("name"),
#             progress=payload.get("progress"),
#             description=payload.get("description"),
#         )
#         return JsonResponse({'mess':"sucsess"})
#     except:
#         return JsonResponse({'mess':"fail"}, status=404)
    


# def add_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')
#     else:
#         form = ContactForm()

#     return render(request, 'add_contact.html', {'form': form})


# def contact_list(request):
#     contacts = Contact.objects.all()

#     return render(request, 'contact_list.html', {
#         'contacts': contacts
#     })







def seed_lib(request):
    reader1 = Reader.objects.create(
        first_name="Ivan",
        last_name="Petrenko",
        phone="+380111111111",
        email="ivan@gmail.com"
    )

    reader2 = Reader.objects.create(
        first_name="Oleg",
        last_name="Shevchenko",
        phone="+380222222222",
        email="oleg@gmail.com"
    )

    Book.objects.create(
        title="Harry Potter",
        author="J.K.Rowling",
        publish_year=2001,
        genre="Fantasy",
        publisher="Bloomsbury",
        reader=reader1
    )

    Book.objects.create(
        title="Sherlock Holmes",
        author="Arthur Conan Doyle",
        publish_year=1892,
        genre="Detective",
        publisher="Ward Lock"
    )

    return HttpResponse("Database seeded")


@login_required
def all_books(request):
    books = Book.objects.all().values(
        'id',
        'title',
        'author',
        'publish_year',
        'genre',
        'publisher',
        'is_available'
    )

    return JsonResponse(list(books), safe=False)


@login_required
def available_books(request):
    books = Book.objects.filter(is_available=True).values(
        'id',
        'title',
        'author',
        'publish_year',
        'genre',
        'publisher'
    )

    return JsonResponse(list(books), safe=False)


@login_required
@permission_required('app.view_reader', raise_exception=True)
def all_readers(request):
    readers = Reader.objects.all().values(
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'registration_date'
    )

    return JsonResponse(list(readers), safe=False)


@login_required
@permission_required('app.view_reader', raise_exception=True)
def reader_books(request, pk):
    try:
        reader = Reader.objects.prefetch_related('books').get(id=pk)

        books = reader.books.all().values(
            'id',
            'title',
            'author',
            'publish_year',
            'genre',
            'publisher'
        )

        return JsonResponse(list(books), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse(
            {'error': 'Reader not found'},
            status=404
        )
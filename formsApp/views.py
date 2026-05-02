from django.shortcuts import render
from . import forms


def index(request):
    return render(request, "django_form.html", {"forms": forms.UserForm()})


def postuser(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        surname = request.POST.get("surname", "")
        languages = request.POST.getlist("languages")
        password = request.POST.get("password", "")

        if len(name) < 3 or len(surname) < 3:
            return render(request, "user_page.html", {
                "error_message": "Please enter a name and surname (min 3 characters)"
            })

        return render(request, "user_page.html", {
            "name": name,
            "surname": surname,
            "languages": languages
        })

    return render(request, "form_page.html", {"form": forms.UserForm()})


def user_form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        surname = request.POST.get("surname", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        languages = request.POST.getlist("languages")

        return render(request, "user_page.html", {
            "name": name,
            "surname": surname,
            "email": email,
            "phone": phone,
            "languages": languages
        })

    return render(request, "buyerForm.html", {"form": forms.UserForm()})


def seller_form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        surname = request.POST.get("surname", "")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        employment_date = request.POST.get("employment_date", "")
        position = request.POST.get("position", "")

        return render(request, "seller_page.html", {
            "name": name,
            "surname": surname,
            "phone": phone,
            "email": email,
            "employment_date": employment_date,
            "position": position
        })

    return render(request, "sellerForm.html")


def product_form(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name", "")
        product_description = request.POST.get("product_description", "")

        return render(request, "product_page.html", {
            "product_name": product_name,
            "product_description": product_description
        })

    return render(request, "itemForm.html")


def sales_form(request):
    if request.method == "POST":
        buyer = request.POST.get("buyer", "")
        seller = request.POST.get("seller", "")
        product = request.POST.get("product", "")
        sale_date = request.POST.get("sale_date", "")
        sale_amount = request.POST.get("sale_amount", "")

        return render(request, "sales_page.html", {
            "buyer": buyer,
            "seller": seller,
            "product": product,
            "sale_date": sale_date,
            "sale_amount": sale_amount
        })

    return render(request, "salesForm.html")
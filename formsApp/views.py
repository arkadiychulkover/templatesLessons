from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import forms
from django.conf import settings
from .forms import UserForm
from datetime import datetime
import os

userForm = UserForm()

def current_time():
    return str(int(datetime.timestamp(datetime.now())))

def index(request):
    return render(request, "django_form.html", {"forms": forms.UserForm()})


# def postuser(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "")
#         surname = request.POST.get("surname", "")
#         languages = request.POST.getlist("languages")
#         password = request.POST.get("password", "")
#
#         if len(name) < 3 or len(surname) < 3:
#             return render(request, "user_page.html", {
#                 "error_message": "Please enter a name and surname (min 3 characters)"
#             })
#
#         return render(request, "user_page.html", {
#             "name": name,
#             "surname": surname,
#             "languages": languages
#         })
#
#     return render(request, "form_page.html", {"form": forms.UserForm()})


def postuser(request:HttpRequest):
    if request.method == "POST":
        form = forms.UserForm(request.POST, request.FILES)
        print("POST")
        if form.is_valid():
            print("valid")
            print(form.cleaned_data)
            name = form.cleaned_data.get("name", "")
            surname = form.cleaned_data.get("surname", "")
            avatar = form.cleaned_data.get("avatar", "")
            print("Avatar")
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_type = avatar.name.split(".")[1]
            file_name = fs.save(f"{current_time()}.{file_type}", avatar)

            return render(request, "user_page.html", {"name": name, "surname": surname, "imageUrl": fs.url(file_name)})

        global userForm
        userForm = form
        return render("form_page")


    else:
        return HttpResponseNotAllowed("not allowed")


def postwater(request: HttpRequest):
    if request.method == "GET":
        return render(request, "django.html", {"form": forms.WaterForm()})

    if request.method == "POST":
        name = request.POST.get("name", "")
        surname = request.POST.get("surname", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")
        months = request.POST.get("months", "")
        volume = request.POST.get("volume", "")

        if len(name) < 2 or len(surname) < 2:
            return render(request, "form_page.html", {
                "error_message": "Name and surname must be at least 2 characters"
            })

        request.session["water_data"] = {
            "name": name,
            "surname": surname,
            "email": email,
            "phone": phone,
            "address": address,
            "months": months,
            "volume": volume,
            "notes": request.POST.get("notes", "")
        }
        return redirect("water_result")

    return HttpResponseNotAllowed(["GET", "POST"])


def water_result(request: HttpRequest):
    data = request.session.get("water_data", None)
    if not data:
        return redirect("postwater")
    return render(request, "water_page.html", data)

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
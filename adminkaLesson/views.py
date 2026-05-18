from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotAllowed, HttpRequest
from .form import RegistrationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def register_page(request: HttpRequest):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form, "button": "Register", "action": 'registration_view'})
    

def register_view(request: HttpRequest) :
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth_page')
    else:
        print(form.errors)
        return redirect('register_page')
    return HttpResponseNotAllowed(['POST'])

def login_page(request):
    if request.user_is_authenticated:
        return redirect("auth_page")
    return render(request, "register.html", {"form": AuthenticationForm(), "button": "Login", "action": 'login_view'})

def login_view(request: HttpRequest):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('auth_page')
        else:
            print(form.errors)
            return redirect('login_page')
    return HttpResponseNotAllowed(['POST'])


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login_page')


@login_required
def auth_page(request: HttpRequest):
    return render(request, 'auth.html', {'user': request.user})
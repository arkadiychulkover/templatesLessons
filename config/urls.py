"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ViewTemplate import views
from config import settings

urlpatterns = [
   # path('admin/', admin.site.urls),
   path("templates/", include("ViewTemplate.urls")),
   path("forms/", include("formsApp.urls")),
   path("models/", include("modelsApp.urls")),
   # path("", views.hello_world_eng, name="index"),
   # path("<str:lan>/", views.hello_world, name="helloWorld"),
   # path("", views.sport_index, name="index"),
   # path("football/", views.football, name="football"),
   # path("hockey/", views.hockey, name="hockey"),
   # path("basketball/", views.basketball, name="basketball"),
   path('', views.recipes, name='recp'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
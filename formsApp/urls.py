from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

urlpatterns = [
    path("", views.index, name="form_page"),
    path("water/", views.postwater, name="postwater"),
    path("water/result/", views.water_result, name="water_result"),
    path("simple_form/", views.postuser, name="simple_form"),
    path("postuser/", views.postuser, name="about"),
    path("user/", views.user_form, name="user_form"),
    path("seller/", views.seller_form, name="seller_form"),
    path("product/", views.product_form, name="product_form"),
    path("sales/", views.sales_form, name="sales_form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
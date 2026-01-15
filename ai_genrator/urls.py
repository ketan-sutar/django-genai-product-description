from django.urls import path,include
from .views import home , bulk_Create_ProductDetails, generate_single_product_details

urlpatterns = [
    path('home/', home, name='home'),
    path('generate-single/', generate_single_product_details, name='generate-single'),
    path("bulk-generate/",bulk_Create_ProductDetails, name="bulk-generate"),
]
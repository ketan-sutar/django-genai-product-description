from django.urls import path,include
from .views import home , bulk_Create_ProductDetails, generate_single_product_details
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('home/', home, name='home'),
    path('generate-single/', generate_single_product_details, name='generate-single'),
    path("bulk-generate/",bulk_Create_ProductDetails, name="bulk-generate"),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
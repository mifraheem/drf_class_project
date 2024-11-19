
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path
from .views import example_view
from .views import regsiter_user
from store.views import create_product, get_user_products

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/register/', regsiter_user),


    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_data/', example_view, name='test_token'),


    path('api/add-product/', create_product),
    path('api/user-products/', get_user_products)

]


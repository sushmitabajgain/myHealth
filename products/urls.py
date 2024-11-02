from django.urls import path
from .views import product_list, home  # Import home view

urlpatterns = [
    path('', home, name='home'),  # URL for the home view
    path('products/', product_list, name='product_list'),  # URL for the product list view
]

from django.shortcuts import render
from .models import Product  # Import the Product model

def home(request):
    """Home page view."""
    return render(request, 'products/home.html')  # Render the home.html template

def product_list(request):
    """View to list all products."""
    products = Product.objects.all()  # Retrieve all products from the database
    context = {
        'products': products,  # Pass the products to the template
    }
    return render(request, 'products/product_list.html', context)  # Render product_list.html

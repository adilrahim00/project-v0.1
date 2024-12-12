from django.shortcuts import render, get_object_or_404
from .models import Product  # Assuming you have a Product model defined

def index(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'index.html', {'products': products})

def product_detail(request, product_id):
    # Fetch the product with the given ID or show 404 if not found
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request):
    # Example cart view (to be implemented)
    return render(request, 'add_to_cart.html')

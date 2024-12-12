from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage listing all products
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Product details page
    path('cart/', views.add_to_cart, name='add_to_cart'),  # Add to cart page
]

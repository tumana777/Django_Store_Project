from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product

def product_list(request):
    products = [f"id: {str(product.pk)} - {product.name}" for product in Product.objects.all()]
    return HttpResponse(f"<h3>Here are all products in store({len(products)}):</h3>\n{'; '.join(products)}")

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return JsonResponse(
        {
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        }
    )
from django.http import JsonResponse
from .models import Category, Product
from django.utils import timezone

def category_list(request):
    categories = Category.objects.all()

    category_json = [
        {
            "ID": category.id,
            "Name": category.name,
            "Parent": {"ID": category.parent.id,
                       "Name": category.parent.name} if category.parent else "No Parent Category"
        }
        for category in categories
    ]

    return JsonResponse({"Categories": category_json})

def product_list(request):
    products = Product.objects.all()

    product_json = [
        {
            "ID": product.id,
            "Name": product.name,
            "Description": product.description,
            "Price": product.price,
            "Quantity": product.quantity,
            "Created": timezone.localtime(product.created_at).strftime("%Y-%m-%d %H:%M:%S"),
            "Updated": timezone.localtime(product.updated_at).strftime("%Y-%m-%d %H:%M:%S"),
            "Category": [category.name for category in product.category.all()],
            "Image URL": request.build_absolute_uri(product.image.url) if product.image else "No Image"
        }
        for product in products
    ]

    return JsonResponse({"Products": product_json})
from django.shortcuts import render
from .models import Category, Product
from django.db.models import F, Max, Avg, Min, Sum


def category_list(request):
    categories = Category.objects.filter(parent=None)

    for category in categories:
        all_categories = category.get_descendants(include_self=True)
        products_count = Product.objects.filter(category__in=all_categories).count()
        category.products_count = products_count

    return render(request, 'categories.html', {"categories": categories})

def product_list(request, category_id):
    main_category = Category.objects.get(id=category_id)

    all_categories = main_category.get_descendants(include_self=True)

    products = (Product.objects.filter(category__in=all_categories)
                .prefetch_related('category').distinct()
                .annotate(total=F('quantity') * F('price')))

    for product in products:
        print(product.total)

    stats = products.aggregate(max_price=Max('price'),
                               min_price=Min('price'),
                               avg_price=Avg('price'),
                               total_sum=Sum(F('quantity') * F('price')))

    context = {
        'products': products,
        'stats': stats,
    }


    return render(request, 'products.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {"product": product})
from django.urls import path
from .views import category_list, product_list, product_detail

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/<int:category_id>/products', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail')
]
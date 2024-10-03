from django.contrib import admin
from .models import Product

admin.site.register(Product)

admin.site.site_header = "Store Administration"

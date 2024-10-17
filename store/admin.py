from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_select_related = ('parent',)
    list_per_page = 20

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'get_total', 'created_at', 'updated_at')
    list_filter = ('created_at', 'price', 'quantity')
    search_fields = ('name', 'price', 'quantity')
    list_editable = ('price', 'quantity')
    list_per_page = 10

    @admin.display(description='Total Price')
    def get_total(self, obj):
        return obj.quantity * obj.price

admin.site.site_header = "Store Administration"

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'category'

    def __str__(self):
        if self.parent:
            return f"{self.parent} -> {self.name}"
        else:
            return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ManyToManyField('store.Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'product'

    def __str__(self):
        return self.name
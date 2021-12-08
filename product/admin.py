from django.contrib import admin
from product.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "units_sold", "in_stock", "expire_date"]

admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
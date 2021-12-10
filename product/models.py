from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=155)
    units_sold = models.CharField(max_length=155)
    in_stock = models.CharField(max_length=155)
    expire_date = models.DateField()
    category = models.ForeignKey("product.Category",on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='media/product', blank=True,null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ["id"]


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]



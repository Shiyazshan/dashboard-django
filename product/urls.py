from django.urls import path
from product.views import product,category
from product import views


app_name = "product"


urlpatterns = [
    path('', product, name="product"),
    path("category/",category, name="category"),
    path("add-product/",views.add_product, name="add_product"),

]
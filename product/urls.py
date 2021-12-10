from django.urls import path
from product.views import product,category,del_product
from product import views


app_name = "product"


urlpatterns = [
    path('', product, name="product"),
    path("category/",category, name="category"),
    path("add-product/",views.add_product, name="add_product"),
    path("del_product/<pk>/",del_product,name="del_product")

]
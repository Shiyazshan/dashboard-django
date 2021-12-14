from django.urls import path
from product.views import product,category,del_product,update,del_category
from product import views


app_name = "product"


urlpatterns = [
    path('', product, name="product"),
    path("category/",category, name="category"),
    path("add-product/",views.add_product, name="add_product"),
    path("edit-product/<pk>/",views.edit_product, name="edit_product"),
    path("del_product/<pk>/",del_product,name="del_product"),
    path("del_category/<pk>/",del_category,name="del_category"),

    path("update/<pk>/",update,name="update"),
]
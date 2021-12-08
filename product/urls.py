from django.urls import path
from product.views import product


app_name = "product"


urlpatterns = [
    path('', product, name="product" )
]
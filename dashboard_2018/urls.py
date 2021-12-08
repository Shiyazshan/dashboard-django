from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls",namespace="web")),
    path('product/', include("product.urls",namespace="product")),
    path('user/', include("user.urls",namespace="user")),
]
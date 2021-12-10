from django import forms
from django.shortcuts import render
from django.http import JsonResponse
from product.forms import ProductForm
from product.models import Product


from product.models import Product,Category


def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category_name = request.GET.get('category')

    context = {
    'products' : products,
    'categories' : categories,
    'category_name' : category_name,
    }

    return render(request, "products.html",context=context)


def category(request):
    category_name =request.GET.get('category')
    if category_name:

        if category_name == "All":

            products = Product.objects.all().values()
            data = list(products)  
            response_data = {
                "title" : "success",
                "data" : data,
            }
        elif Category.objects.filter(name=category_name).exists():
            if Product.objects.filter(category__name=category_name).exists():
                products = Product.objects.filter(category__name=category_name).values()
                data = list(products)  

                response_data = {
                    "title" : "success",
                    "data" : data,
                }
            else:
                response_data = {
                    "title" : "failed",
                    "message" : "Projects not found",
                }
        else:
            response_data = {
                "title" : "failed",
                "message" : "Category not found",
            }
    else:
        response_data = {
            "title" : "failed",
            "message" : "Category not found",
        }

    return JsonResponse({'response_data': response_data})

def add_product(request):
    form = ProductForm(request.POST, request.FILES,)
    if form.is_valid():
        form.save()
    else:
        print("errror=======================", form.errors)

    return render(request, 'add-product.html',{'form':form})
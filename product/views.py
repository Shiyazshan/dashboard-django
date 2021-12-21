from django import forms
from django.shortcuts import redirect,render
from django.http import JsonResponse
from product.forms import ProductForm
from product.models import Product,Category
from product.functions import generate_form_errors
from django.views.generic import View



def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category_name = request.GET.get('category')

    context = {
    'products' : products,
    'categories' : categories,
    'category_name' : category_name,
    }

    return render(request, "products.html", context=context)


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

    return render(request, 'add-product.html',{'form':form})

def del_product(request,pk):
    products = Product.objects.filter(pk=pk)
    products.delete()

    return redirect("product:product")

def del_category(request,pk):
    categories = Category.objects.filter(pk=pk)
    categories.delete()

    return redirect("product:product")

def edit_product(request, pk):  
    product = Product.objects.get(pk=pk)  
    form = ProductForm(instance = product)  

    context = {
        "product" : product,
        "form" : form
    }

    return render(request,'edit-product.html',context=context) 

def update(request, pk):  
    product = Product.objects.get(pk=pk) 
    form = ProductForm(request.POST, request.FILES, instance = product)  

    if form.is_valid():  
        form.save()  
        return redirect("product:product")  

    return render(request, 'edit-product.html', {'product':product})  

class Product_view(View):
    def get(self,request):
        products=Product.objects.all()
        context ={
            "products":products,
        }
        return render(request,"product.html", context=context)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            product_ids=request.POST.getlist('id[]')
            for id in product_ids:
                product=Product.objects.get(pk=id)
                product.delete()
            return redirect("product:product")
        return render(request,"product.html")
        

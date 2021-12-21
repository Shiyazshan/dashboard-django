from django import forms
from django import forms
from product.models import Product,Category
from django.forms.widgets import DateInput


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Product
        exclude = ('units_sold',)
        widgets = {
            'expire_date' : DateInput(attrs={'type':'date'}),
        }
        error_messages = {
            'product_name' : {
                'required' :("product_name field is required."),
            },
            'in_stock' : {
                'required' :("in_stock field is required."),
            },
            'description' : {
                'required' :("description field is required."),
            },
            'exp_date' : {
                'required' : ("exp_date field is required."),
            },
            'category' : {
                'required' : ("category field is required."),
            },
            'category' : {
                'required' : ("category field is required."),
            },
            'image' : {
                'required' : ("image field is required."),
            },
        }
        
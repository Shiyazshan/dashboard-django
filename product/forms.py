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
        
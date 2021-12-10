from django import forms
from django import forms
from product.models import Product,Category


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    # image = forms.ImageField()
    class Meta:
        model = Product
        exclude = ('units_sold',)
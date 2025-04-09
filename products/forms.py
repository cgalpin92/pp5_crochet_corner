from django import forms
from .models import Product, ProductCategory, ToolCategory, YarnCategory, ToolBrand, YarnBrand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

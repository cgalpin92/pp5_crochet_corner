from django import forms
from .widgets import CustomClearableFileInput
from .models import Product
from checkout.models import Order


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

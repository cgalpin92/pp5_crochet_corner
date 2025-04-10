from django import forms
from .widgets import CustomClearableFileInput
from .models import Product
from checkout.models import Order


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


class AdminOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'street_address1', 'street_address2', 'town_or_city',
                  'postcode', 'country', 'county', 'order_status')

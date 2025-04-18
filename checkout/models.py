import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Stores the entire order generated
    by the user
    """
    PENDING = "Pending"
    DISPATCHED = "Dispatched"
    RETURN_PENDING = "Return Pending"
    RETURNED = "Returned"
    ORDER_STATUS_CHOICES = [
        (PENDING, "Pending"),
        (DISPATCHED, "Dispatched"),
        (RETURN_PENDING, "Return Pending"),
        (RETURNED, "Returned"),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    order_status = models.CharField(max_length=20,
                                    choices=ORDER_STATUS_CHOICES,
                                    default=PENDING)
    original_basket = models.TextField(null=False, blank=True, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=True,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total')
                                                    )['lineitem_total__sum'
                                                        ''] or 0
        if self.order_total < settings.FREE_DELIVERY_LIMIT:
            self.delivery_cost = (self.order_total *
                                  settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number if it hasn't
        been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    stores the individual order item
    has relationships with Order and Product
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    product_name = models.CharField(max_length=100, help_text='records'
                                    'product name at time of creation which '
                                    'will not change when product is updated')

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total and update
        the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        self.product_name = self.product.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total',
                       'grand_total', 'original_basket', 'stripe_pid')

    fields = ('order_number', 'date', 'first_name', 'last_name',
              'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2',
              'county', 'delivery_cost', 'order_total',
              'grand_total', 'order_status', 'original_basket', 'stripe_pid')
    
    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'delivery_cost', 'grand_total',
                    'order_status',)
    
    ordering = ('-date',)

    list_filter = ('order_status',)

    search_fields = ('order_status', 'last_name',)


admin.site.register(Order, OrderAdmin)
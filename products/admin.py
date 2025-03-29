from django.contrib import admin
from .models import ProductCategory, YarnCategory, ToolCategory, YarnBrand, ToolBrand, Product

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(YarnCategory)
admin.site.register(ToolCategory)
admin.site.register(YarnBrand)
admin.site.register(ToolBrand)
admin.site.register(Product)

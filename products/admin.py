from django.contrib import admin
from .models import ProductCategory, YarnCategory, ToolCategory, YarnBrand, ToolBrand, Product

# Register your models here.


class YarnCategoryAdmin(admin.ModelAdmin):
    ordering = ['yarn_category_name']


class ToolCategoryAdmin(admin.ModelAdmin):
    ordering = ['tool_category_name']


class YarnBrandAdmin(admin.ModelAdmin):
    ordering = ['name']


class ToolBrandAdmin(admin.ModelAdmin):
    ordering = ['name']


class ProductAdmin(admin.ModelAdmin):
    ordering = ['-sku']
    list_filter = ('product_category', 'yarn_category', 'yarn_brand', 'tool_category', 'tool_brand')
    list_display = ('name', 'sku', 'price', 'image')
    search_fields = ['name']


admin.site.register(ProductCategory)
admin.site.register(YarnCategory, YarnCategoryAdmin)
admin.site.register(ToolCategory, ToolCategoryAdmin)
admin.site.register(YarnBrand, YarnBrandAdmin)
admin.site.register(ToolBrand, ToolBrandAdmin)
admin.site.register(Product, ProductAdmin)

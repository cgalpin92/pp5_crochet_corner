from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class YarnCategory(models.Model):
    yarn_category_name = models.CharField(max_length=200)
    yarn_friendly_name = models.CharField(max_length=200)

    def __str__(self):
        return self.yarn_category_name
    
    def get_friendly_name(self):
        return self.yarn_friendly_name


class ToolCategory(models.Model):
    tool_category_name = models.CharField(max_length=200)
    tool_friendly_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tool_category_name
    
    def get_friendly_name(self):
        return self.tool_friendly_name


class YarnBrand(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class ToolBrand(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    BLACK = "Black"
    GREY = "Grey"
    WHITE = "White"
    RED = "Red" 
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"
    BROWN = "Brown"
    MULTI = "Multi"
    COLOR_CHOICES = [
        (BLACK, "Black"),
        (GREY, "Grey"),
        (WHITE, "White"),
        (RED, "Red"),
        (BLUE, "Blue"),
        (GREEN, "Green"),
        (YELLOW, "Yellow"),
        (ORANGE, "Orange"),
        (PINK, "Pink"),
        (PURPLE, "Purple"),
        (BROWN, "Brown"),
        (MULTI, "Multi")
    ]
    product_category = models.ForeignKey('ProductCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    yarn_category = models.ForeignKey('YarnCategory', null=True, blank=True, on_delete=models.SET_NULL)
    tool_category = models.ForeignKey('ToolCategory', null=True, blank=True, on_delete=models.SET_NULL)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default=MULTI)
    yarn_brand = models.ForeignKey('YarnBrand', null=True, blank=True, on_delete=models.SET_NULL)
    tool_brand = models.ForeignKey('ToolBrand', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

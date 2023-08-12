from django.db import models

from colorfield.fields import ColorField


class Color(models.Model):
    name = models.CharField(max_length=50)
    code = ColorField()
    
    def __str__(self):
        return self.code

class Size(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category/")
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=False,null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_category'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="subcategory/")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=False,null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_subcategory'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    sku = models.CharField(max_length=100)
    sub_category = models.ForeignKey("SubCategory", on_delete=models.CASCADE)
    weight =  models.CharField(max_length=100)
    dimensions =  models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=10)
    price = models.PositiveIntegerField(default=300)
    discount =models.PositiveIntegerField(null=True, blank=True)
    other_info = models.CharField(max_length = 500)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    
    class Meta:
        managed = True
        db_table = 'tbl_product'

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    
    class Meta:
        managed = True
        db_table = 'tbl_product_image'

    def __str__(self):
        return self.product.name + " - " + str(self.id)

from django.db import models
from PIL import Image,ImageFilter
from colorfield.fields import ColorField
from accounts.models import *
from accounts.constants import *

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


    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'tbl_category'




class SubCategory(models.Model):
    name = models.CharField(max_length=50)
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
    rating = models.PositiveIntegerField(default = 0)

    def calculate_discount_percentage(self):
        if self.price > 0:
            discount = self.price - self.discount if self.discount else 0
            return (discount / self.price) * 100
        return 0

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


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    class Meta:
        managed = True
        db_table = 'tbl_wishlist'



class Ratings(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    rating = models.PositiveIntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    class Meta:
        managed = True
        db_table = 'tbl_ratings'


class Cart(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    run_time_coupan = models.PositiveIntegerField(blank=True,null=True)
    coupans = models.ForeignKey('Coupans',blank=True,null=True,on_delete=models.SET_NULL)

    class Meta:
        managed = True
        db_table = 'tbl_cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length = 500)
    size = models.CharField(max_length = 500)
    color = models.CharField(max_length = 500)
    price = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=1)  
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
      
    class Meta:
        managed = True
        db_table = 'tbl_cart_product'

class Order(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    state = models.CharField(max_length = 500)
    city = models.CharField(max_length = 500)
    zipcode = models.CharField(max_length = 500)
    message = models.CharField(max_length = 500)
    discounted_price = models.PositiveIntegerField(blank=True,null=True)
    grand_total = models.PositiveIntegerField(blank=True,null=True)
    coupan = models.ForeignKey('Coupans',on_delete=models.CASCADE,blank=True,null=True)
    status = models.PositiveIntegerField(default=ADMIN,choices=ORDER_STATUS,null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)


    class Meta:
        managed = True
        db_table = 'tbl_order'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length = 500)
    size = models.CharField(max_length = 500)
    color = models.CharField(max_length = 500)
    price = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'tbl_orderItems'


class Coupans(models.Model):
    name =models.CharField(max_length = 500)
    percentage = models.PositiveIntegerField(default=1)
    count = models.CharField(max_length = 500,default=0)
    expiry_days = models.PositiveIntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_coupans'


    def __str__(self):
        return self.name
from django.contrib import admin
from .models import *
from PIL import Image
from io import BytesIO
import base64
from django.utils.html import format_html
from .models import Product, Color
from django.forms.widgets import CheckboxSelectMultiple
from django import forms
from PIL import Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','TitleImage','created_on','updated_on')
    def TitleImage(self, obj):
        if obj.image:
            image = Image.open(obj.image.path)

            if image.mode != 'RGB':
                image = image.convert('RGB')

            image.thumbnail((100, 100))  # Set your desired thumbnail size
            thumbnail_io = BytesIO()
            image.save(thumbnail_io, format='JPEG')
            thumbnail_data = base64.b64encode(thumbnail_io.getvalue()).decode('utf-8')
            return format_html('<img src="data:image/jpeg;base64,{}" width="100" height="100" />',
                               thumbnail_data)
        return "No Image"

    TitleImage.short_description = 'Image'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','created_on','updated_on')
    

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 4
    extra = 0  



class ProductForm(forms.ModelForm):
    colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=CheckboxSelectMultiple,
    )
    sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=CheckboxSelectMultiple,
    )

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name','sub_category','quantity','price','materials','display_colors','created_on')
    inlines = [ProductImageInline]

    def display_colors(self, obj):
        return ", ".join([color.code for color in obj.colors.all()])

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        product_images = ProductImage.objects.filter(product = obj)

        for image_obj in product_images:
            img = Image.open(image_obj.image.path)
            target_size = (270, 310)
            img.thumbnail(target_size)
            img = img.crop((0, 0, target_size[0], target_size[1]))
            img.save(image_obj.image.path)

    display_colors.short_description = 'Colors'


class RatingsAdmin(admin.ModelAdmin):
    list_display = ('name','email','rating','created_on')

    def has_add_permission(self, request):
        return False 

# class OrderItemsInline(admin.TabularInline):
#     model = OrderItems

#     def has_add_permission(self, request):
#         return False 


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id','first_name','last_name','email','city','created_on')
#     readonly_fields = ('id','first_name','last_name','email','phone','created_on','address','city','state','zipcode','message','created_by')
#     inlines = [OrderItemsInline]



#     def has_add_permission(self, request):
#         return False 

class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 0
    readonly_fields = ['id','product', 'quantity','size','color','price','total_price','created_by','product_image']  # Add other fields if needed
    can_delete = False
    def product_image(self, instance):
        product_images = instance.product.productimage_set.all()
        if product_images.exists():
            image_url = product_images.first().image.url
            return format_html('<img src="{}" width="100" height="100" />', image_url)
        return 'No Image'

    product_image.short_description = 'Product Image'
    product_image.allow_tags = True
    product_image.short_description = 'Product Image'
    def has_add_permission(self, request):
        return False 

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','grand_total','created_on')
    readonly_fields = ('id','first_name','last_name','email','phone','created_on','address','city','state','zipcode','message','discounted_price','grand_total','coupan','created_by')
    inlines = [OrderItemInline]

    def has_add_permission(self, request):
        return False 

class CoupansAdmin(admin.ModelAdmin):
    list_display = ('id','name','percentage','count','expiry_days','created_on',) 


admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Ratings,RatingsAdmin)
admin.site.register(Order,OrderAdmin)

admin.site.register(Coupans,CoupansAdmin)


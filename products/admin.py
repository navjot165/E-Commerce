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

        for image_obj in obj.images.all():
            img = Image.open(image_obj.image.path)
            target_size = (270, 310)
            img.thumbnail(target_size)
            img = img.crop((0, 0, target_size[0], target_size[1]))
            img.save(image_obj.image.path)

    display_colors.short_description = 'Colors'


admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Color)


from django.contrib import admin
from .models import *
from PIL import Image
from io import BytesIO
import base64
from django.utils.html import format_html


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title','TitleImage','seen','created_on')
    actions = ['preview_images']


    def TitleImage(self, obj):
        if obj.title_image:
            image = Image.open(obj.title_image.path)

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


admin.site.register(Blogs, BlogsAdmin)



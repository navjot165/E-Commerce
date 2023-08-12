from .views import *
from django.urls import re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

app_name = 'products'


urlpatterns = [
    re_path(r'^shop/(?P<id>\d+)$', shop_list, name='shop'),
    re_path(r'^shop-product-detail/(?P<id>\d+)$', shop_product_detail, name='shop_product_detail'),
    re_path(r'^cart-detail$', cart_details, name='cart_details'),
    re_path(r'^wishlist$', wishlist_details, name='wishlist'),
    re_path(r'^checkout$', checkout, name='checkout'),

]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

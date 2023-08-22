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
    re_path(r'^user-wishlist$', user_wishlist, name='user_wishlist'),
    re_path(r'^checkout$', checkout, name='checkout'),
    re_path(r'^rating/(?P<id>\d+)$', rating, name='rating'),
    re_path(r'^add-to-cart/(?P<id>\d+)$', add_to_cart, name='add_to_cart'),
    re_path(r'^remove-to-cart/(?P<id>\d+)$', clear_one_cart, name='remove_to_cart'),
    re_path(r'^clear-cart$', clear_cart, name='clear_cart'),
    re_path(r'^update-cart$', update_cart, name='update_cart'),
    re_path(r'^place-order$', placeOrder, name='placeorder'),
    re_path(r'^apply-code$', apply_promocode, name='apply_code'),

]
  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

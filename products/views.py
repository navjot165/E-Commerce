from django.shortcuts import render
from .models import *


def shop_list(request):
    return render(request, 'products/shop-left-sidebar.html')

def shop_product_detail(request,id):
    product = Product.objects.get(id = id )
    related_product = Product.objects.filter(sub_category = product.sub_category ).order_by('-id')[0:6]
    return render(request, 'products/single-product.html', { "data":product,"related_product":related_product })

def cart_details(request):
    return render(request, 'products/cart.html')

def wishlist_details(request):
    return render(request, 'products/wishlist.html')

def checkout(request):
    return render(request, 'products/checkout.html')

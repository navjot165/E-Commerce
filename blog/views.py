from django.shortcuts import render,redirect
from .models import *
from products.models import *

def blog_list(request):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    blog = Blogs.objects.all().order_by("-id")[:9]
    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
    except:
        cart_list = None
    return render(request, 'blog/blog-grid.html',{"blogs":blog,"wish_list":wish_list,"shop_data":shop_data,"cart_list":cart_list,})


def blog_details(request,id):
    shop_data = []
    category = Category.objects.all()
    for i in category:
        s_c = []
        sub_cats = SubCategory.objects.filter(category_id = i.id )
        for j in sub_cats:
            s_c.append({"name":j.name,"id":j.id})
        print(sub_cats)
        shop_data.append({
            "name":i.name,
            "sub_cat":s_c
        })
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    blog = Blogs.objects.get(id = id)
    try:
        cart_list = CartItem.objects.filter(created_by = request.user)
    except:
        cart_list = None
    return render(request, 'blog/blog-single.html',{"blog":blog,"wish_list":wish_list,"shop_data":shop_data,"cart_list":cart_list,})






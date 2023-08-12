from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages



def shop_list(request,id):


    product = Product.objects.filter(sub_category__category_id = id )
    size = Size.objects.all()
    sub_cat_name,subcat_items,sub_cat_id = [],[],[]
    subcat = SubCategory.objects.filter(category_id = id)
    for i in subcat:
        product_count = product.filter(sub_category = i).count()
        subcat_items.append(product_count)
        sub_cat_name.append(i.name)
        sub_cat_id.append(i.id)
    subcat_data = zip(sub_cat_id,sub_cat_name,subcat_items)
    if request.GET.get("search"):
        product = product.filter(name__icontains = request.GET.get("search"))
    if request.GET.get("sort"):
        if request.GET.get("sort") == "1":
            product = product.filter().order_by("name")
        if request.GET.get("sort") == "2":
            product = product.filter().order_by("-name")
        if request.GET.get("sort") == "3":
            product = product.filter().order_by("price")
        if request.GET.get("sort") == "4":
            product = product.filter().order_by("-price")
    if request.GET.get("cat"):
        product = product.filter(sub_category_id = request.GET.get("cat"))
    if request.GET.get("size"):
        product = product.filter(sizes__id__in=request.GET.get("size"))
    if request.GET.get("price"):
        s_p = request.GET.get("price").split('-')[0]
        l_p = request.GET.get("price").split('-')[1]
        product = product.filter(price__range=(int(request.GET.get("price").split('-')[0]),int(request.GET.get("price").split('-')[1])))
        return render(request, 'products/shop-left-sidebar.html',{"products":product,"size":size,"subcat":subcat_data,
                                                                "id":id, "sort":str(request.GET.get("sort")) if request.GET.get("sort") else "",
                                                                "search":request.GET.get("search") if request.GET.get("search") else "",
                                                                "cat": request.GET.get("cat") if request.GET.get("cat") else "",
                                                                "s_p": s_p if s_p else "",
                                                                "l_p": l_p if l_p else 7000
                                                                })
    return render(request, 'products/shop-left-sidebar.html',{"products":product,"size":size,"subcat":subcat_data,
                                                            "id":id, "sort":str(request.GET.get("sort")) if request.GET.get("sort") else "",
                                                            "search":request.GET.get("search") if request.GET.get("search") else "",
                                                            "cat": request.GET.get("cat") if request.GET.get("cat") else "",
                                                            "s_p": 0,
                                                            "l_p": 7000
                                                            })

def shop_product_detail(request,id):
    product = Product.objects.get(id = id )
    related_product = Product.objects.filter(sub_category = product.sub_category ).order_by('-id')[0:6]
    return render(request, 'products/single-product.html', { "data":product,"related_product":related_product })

def cart_details(request):
    return render(request, 'products/cart.html')

def wishlist_details(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.success(request, 'PLease login first to add this item to you wishlist!')
        return redirect('frontend:index')
    return render(request, 'products/wishlist.html')

def checkout(request):
    return render(request, 'products/checkout.html')

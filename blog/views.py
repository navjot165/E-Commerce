from django.shortcuts import render,redirect
from .models import *
from products.models import *

def blog_list(request):
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    blog = Blogs.objects.all().order_by("-id")[:9]
    return render(request, 'blog/blog-grid.html',{"blogs":blog,"wish_list":wish_list})


def blog_details(request,id):
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    blog = Blogs.objects.get(id = id)
    return render(request, 'blog/blog-single.html',{"blog":blog,"wish_list":wish_list})






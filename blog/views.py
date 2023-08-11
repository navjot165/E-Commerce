from django.shortcuts import render,redirect
from .models import *


def blog_list(request):
    blog = Blogs.objects.all().order_by("-id")[:9]
    return render(request, 'blog/blog-grid.html',{"blogs":blog})


def blog_details(request,id):
    blog = Blogs.objects.get(id = id)
    return render(request, 'blog/blog-single.html',{"blog":blog})






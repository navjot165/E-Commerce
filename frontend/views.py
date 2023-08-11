from accounts.models import *
from products.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,redirect



def index(request):
    if request.user.is_authenticated and request.user.is_superuser and (request.user.role_id == 1 ):
        return redirect('admin:index')
    else:
        all_products = Product.objects.all().order_by('id')[0:8]
        new_products = Product.objects.all().order_by('-id')[0:8]
        discounted_products =  Product.objects.filter(discount__isnull = False).order_by('-id')[0:8]
        category = Category.objects.all()
        cat_id,cat_name,cat_image,cat_items=[],[],[],[]
        for cat in category:
            cat_id.append(cat.id)
            cat_name.append(cat.name)
            cat_image.append(cat.image.url)
            product = Product.objects.filter(sub_category__category = cat ).count()
            cat_items.append(product)
        print(cat_id,cat_name,cat_image,cat_items)
        data = zip(cat_id,cat_name,cat_image,cat_items)
        return render(request, 'frontend/index.html',{"data":data,"products":all_products,"new_products":new_products,
                                                    "discounted_products":discounted_products})
    

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    if request.method == "POST":
        contact = ContactUs.objects.create(name = request.POST.get("name"),
                                           email = request.POST.get("email"),
                                           message = request.POST.get("message"))
        messages.success(request, 'Thank you for you enquiry, We will get back to you soon')
        return redirect('frontend:contact_us')
        
    
    return render(request, 'frontend/contact.html')

def login(request):
    return render(request, 'frontend/login.html')


def product_list(request):
    return render(request, 'frontend/shop-left-sidebar.html')



def get_product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_data = {
        'name': product.name,
        'description': product.description,
        # Add more fields as needed
    }
    return JsonResponse(product_data)


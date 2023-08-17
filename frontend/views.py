from accounts.models import *
from products.models import *
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Avg , Count
from django.shortcuts import render,redirect




def index(request):
    if request.user.is_authenticated and request.user.is_superuser and (request.user.role_id == 1 ):
        return redirect('admin:index')
    else:
        try:
            wishlist_products = Wishlist.objects.filter(created_by=request.user).values_list('product', flat=True)
        except:
            wishlist_products = None
        try:
            cart_list = Cart.objects.filter(created_by = request.user)
        except:
            cart_list = None
        rating = Ratings.objects.filter(rating__gt = 4).order_by('-id')[0:3]
        try:
            wish_list = Wishlist.objects.filter(created_by = request.user)
        except:
            wish_list = None

        all_products = Product.objects.all().annotate(
            rating_count=Count('ratings'),
            avg_rating=Avg('ratings__rating')
        ).order_by('id')[0:8]
        for product in all_products:
            if product.avg_rating is not None:
                product.avg_rating *= 20
            else:
                product.avg_rating = 0


        new_products = Product.objects.all().annotate(
            rating_count=Count('ratings'),
            avg_rating=Avg('ratings__rating')
        ).order_by('-id')[0:8]
        for product in new_products:
            if product.avg_rating is not None:
                product.avg_rating *= 20
            else:
                product.avg_rating = 0

        discounted_products =  Product.objects.filter(discount__isnull = False).annotate(
            rating_count=Count('ratings'),
            avg_rating=Avg('ratings__rating')
        ).order_by('-id')[0:8]
        for product in discounted_products:
            if product.avg_rating is not None:
                product.avg_rating *= 20
            else:
                product.avg_rating = 0



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
                                                    "discounted_products":discounted_products,"wish_list":wish_list,"rating":rating,
                                                    "wishlist_products":wishlist_products,"cart_list":cart_list})
    
def about(request):
    rating = Ratings.objects.filter(rating__gt = 4).order_by('-id')[0:3]
    try:
        cart_list = Cart.objects.filter(created_by = request.user)
    except:
        cart_list = None
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    return render(request, 'frontend/about.html',{"wish_list":wish_list,"rating":rating,"cart_list":cart_list})

def contact(request):
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    try:
        cart_list = Cart.objects.filter(created_by = request.user)
    except:
        cart_list = None
    if request.method == "POST":
        contact = ContactUs.objects.create(name = request.POST.get("name"),
                                           email = request.POST.get("email"),
                                           message = request.POST.get("message"))
        messages.success(request, 'Thank you for you enquiry, We will get back to you soon')
        return redirect('frontend:contact_us')
        
    
    return render(request, 'frontend/contact.html',{"wish_list":wish_list,"cart_list":cart_list})

def login(request):
    return render(request, 'frontend/login.html')

def product_list(request):
    return render(request, 'frontend/shop-left-sidebar.html')

def my_account(request):
    try:
        wish_list = Wishlist.objects.filter(created_by = request.user)
    except:
        wish_list = None
    try:
        cart_list = Cart.objects.filter(created_by = request.user)
    except:
        cart_list = None
    user = User.objects.get(id = request.user.id)
    if request.method == "POST":
        if request.POST.get("first_name"):
            user.first_name = request.POST.get("first_name")
            
        if request.POST.get("last_name"):
            user.last_name = request.POST.get("last_name")

        if request.POST.get("mobile_no"):
            user.mobile_no = request.POST.get("mobile_no")

        if request.POST.get("dob"):
            user.dob = request.POST.get("dob")
        user.save()
        messages.success(request, 'Profile updated successfully')
    return render(request, 'frontend/my-account.html',{"wish_list":wish_list,"cart_list":cart_list})

def get_product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_data = {
        'name': product.name,
        'description': product.description,
        # Add more fields as needed
    }
    return JsonResponse(product_data)


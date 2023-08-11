
from .models import *
from frontend.views import *
from datetime import datetime
from user_agents import parse
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View , TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request, 'Log out successfully')
        return redirect('accounts:login')


class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'frontend/login.html')

    def post(self,request,*args,**kwargs):
        print(request.POST.get("password"))
        if User.objects.filter(email = request.POST.get("password")):
            return render(request,'frontend/login.html')
        if User.objects.filter(mobile_no = request.POST.get("mobile_no")):
            return render(request,'frontend/login.html')
        user = User.objects.create( first_name = request.POST.get("first_name"),last_name = request.POST.get("last_name"),
                                    email = request.POST.get("email"),mobile_no = request.POST.get("mobile_no"),role_id = USER,
                                    password = make_password(request.POST.get("password")) )
        
        
        messages.success(request, 'User registered successfully')
        return redirect('frontend:index')

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'frontend/login.html')

    def post(self,request,*args,**kwargs):
        email = request.POST.get("email")

        password = request.POST.get("password")
        des= request.path
        urls="http://"+request.META.get("REMOTE_ADDR")+des
        print(email,password)
        if not email:
            messages.success(request, 'Please enter email')
            return render(request, 'frontend/login.html',{"email":email,"password":password})
        if not password:
            return render(request, 'frontend/login.html',{"email":email,"password":password})
        
        if request.POST.get('remember_me')=='on':    
           request.session.set_expiry(1209600) 
        try:
            user = authenticate(username=email, password=password)
        except Exception as e:
            user = None

        if not user:
            LoginHistory.objects.create(User_Ip=request.META.get("REMOTE_ADDR"),User_agent=str(parse(request.META['HTTP_USER_AGENT'])),State="Failed",Code=urls,user=user)
            messages.success(request, 'Invalid login details.')
            return redirect('frontend:index')

        if user.is_authenticated and  user.role_id == USER:
            login(request, user)
            LoginHistory.objects.create(User_Ip=request.META.get("REMOTE_ADDR"),User_agent=str(parse(request.META['HTTP_USER_AGENT'])),State="Success",Code=urls,user=user)
            messages.success(request, 'Login successfully')
            return redirect('frontend:index')
        
        if user.is_authenticated and user.role_id == ADMIN:
            login(request, user)
            LoginHistory.objects.create(User_Ip=request.META.get("REMOTE_ADDR"),User_agent=str(parse(request.META['HTTP_USER_AGENT'])),State="Success",Code=urls,user=user)
            messages.success(request, 'Login successfully')
            return redirect('admin:index')
        
        return render(request, 'frontend/login.html',{"email":email,"password":password})

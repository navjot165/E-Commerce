from .views import *
from django.contrib import admin
from django.urls import re_path
from django.urls import path

admin.autodiscover()

app_name = 'accounts'

urlpatterns = [

    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogOutView.as_view(), name='logout'),
    re_path(r'^registration/$', RegistrationView.as_view(), name='registration'),
    

]
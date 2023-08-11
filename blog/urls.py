from .views import *
from django.urls import re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

app_name = 'blog'


urlpatterns = [
    re_path(r'^blog-list$', blog_list, name='blog_list'),
    re_path(r'^blog-details/(?P<id>\d+)$', blog_details, name='blog_details'),

]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

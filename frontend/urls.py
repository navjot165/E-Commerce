from .views import *
from .sitemaps import StaticSitemap
from django.urls import re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap


admin.autodiscover()

app_name = 'frontend'


sitemaps = {
 'pages': StaticSitemap,
}

urlpatterns = [
    re_path(r'^sitemap.xml/$', sitemap, {'sitemaps': sitemaps}),
    re_path(r'^$', index, name='index'),
    re_path(r'^about$', about, name='about'),
    re_path(r'^contact-us$', contact, name='contact_us'),
    re_path(r'^login$', login, name='login'),
    re_path(r'^product-list$', product_list, name='product_list'),
    re_path(r'^get-product-details$', get_product_details, name='get_product_details'),
    re_path(r'^my-account$', my_account, name='my_account'),
]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

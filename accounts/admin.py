from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(UserAdmin):
    list_display = ('id','first_name','last_name','email','mobile_no','is_active','created_on')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email','mobile_no','profile_pic','role_id','is_active','status')}),
    )    
    readonly_fields = ('first_name','last_name','email','mobile_no','is_active','created_on')

    change_form_template = 'admin/accounts/custom_change_form.html'
    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Override the change_view method
        extra_context = extra_context or {}
        extra_context['show_save'] = False  # Set show_save to False to hide the "Save" button
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def has_add_permission(self, request):
        return False 


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','created_on')

   
    readonly_fields = ('name','email','created_on','message','created_on',)

    change_form_template = 'admin/accounts/custom_change_form.html'
    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Override the change_view method
        extra_context = extra_context or {}
        extra_context['show_save'] = False  # Set show_save to False to hide the "Save" button
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def has_add_permission(self, request):
        return False 

admin.site.register(User, UserAdmin)
admin.site.register(ContactUs, ContactUsAdmin)



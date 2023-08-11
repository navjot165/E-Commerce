import uuid
from .constants import *
from django.db import models
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255,blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    full_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField("email address", null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    profile_pic = models.FileField(upload_to='profile_pic/', blank=True, null=True)
    role_id = models.PositiveIntegerField(default=ADMIN,choices=USER_ROLE,null=True, blank=True)
    gender = models.CharField(max_length=20,choices=GENDER,null=True, blank=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    zipcode = models.CharField(max_length=255,blank=True,null=True)
    status = models.PositiveIntegerField(default=ACTIVE, choices=USER_STATUS,null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_user'

    def __str__(self):
        return str(self.username)


class LoginHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User_Ip = models.CharField( max_length=255, null=True, blank=True)
    User_agent = models.CharField(max_length=255, null=True, blank=True)
    State = models.CharField(default=timezone.now, max_length=255, null=True, blank=True)
    Code = models.CharField(default=timezone.now, max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    user = models.CharField( max_length=255, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'login_history'




class ContactUs(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'tbl_contact_us'
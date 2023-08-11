from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    title_image = models.ImageField(upload_to='images/')
    second_image = models.ImageField(upload_to='images/')
    third_image = models.ImageField(upload_to='images/')
    first_description = models.TextField()
    second_description = models.TextField()
    seen = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=False,null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_blog'
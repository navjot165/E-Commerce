# Generated by Django 2.2.8 on 2023-08-17 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order_orderitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]

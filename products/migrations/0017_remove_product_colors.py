# Generated by Django 2.2.8 on 2023-08-23 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20230822_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
    ]
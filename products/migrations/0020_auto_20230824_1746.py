# Generated by Django 2.2.8 on 2023-08-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20230824_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='gst',
            field=models.CharField(default='18%', max_length=5),
        ),
    ]
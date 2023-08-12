# Generated by Django 2.2.8 on 2023-08-09 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('sku', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('materials', models.CharField(max_length=100)),
                ('other_info', models.CharField(max_length=500)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SubCategory')),
            ],
            options={
                'db_table': 'tbl_product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'tbl_product_image',
                'managed': True,
            },
        ),
    ]

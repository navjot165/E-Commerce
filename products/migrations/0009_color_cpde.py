# Generated by Django 2.2.8 on 2023-08-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230810_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='cpde',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.8 on 2023-08-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20230819_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupans',
            name='count',
            field=models.CharField(default=0, max_length=500),
        ),
    ]

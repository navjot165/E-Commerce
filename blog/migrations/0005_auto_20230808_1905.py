# Generated by Django 2.2.8 on 2023-08-08 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230808_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='secong_image',
            new_name='second_image',
        ),
    ]
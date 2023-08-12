from django.core.management.base import BaseCommand
from products.models import Size, Color

class Command(BaseCommand):
    help = 'Populate sizes and colors in the database'

    def handle(self, *args, **options):
        sizes = ['S', 'M', 'L','XL','XXL','XXXL']
        color_data = [
            {'code': '#FF0000'},
            {'code': '#0000FF'},
            {'code': '#00FF00'},
            # Add more color data here
        ]

        for size_name in sizes:
            Size.objects.get_or_create(name=size_name)
            self.stdout.write(self.style.SUCCESS(f'Size "{size_name}" added'))

        for color in color_data:
            Color.objects.get_or_create(code=color['code'])
            self.stdout.write(self.style.SUCCESS(f'Color with code {color["code"]} added'))


        self.stdout.write(self.style.SUCCESS('Sizes and colors added successfully'))

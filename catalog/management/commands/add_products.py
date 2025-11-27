from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавление продуктов в базу данных'

    def handle(self, *arg, **options):
        # Удаляем существующие записи

        Product.objects.all().delete()
        Category.objects.all().delete()

        # Добавляем новые записи

        category, _ = Category.objects.get_or_create(name='Ягода', description='Маленький сочный или мясистый плод')

        products = [
            {'name': 'Смородина', 'description': 'Сочная ягода', 'category': category, 'price': 800},
            {'name': 'Малина', 'description': 'Полезная ягода', 'category': category, 'price': 1000},
            {'name': 'Арбуз', 'description': 'Большая ягода', 'category': category, 'price': 400},
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт {product.name} добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт {product.name} уже существует'))

        #  добавляем данные из фикстуры

        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
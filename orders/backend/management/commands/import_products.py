import yaml
import os

from django.core.management.base import BaseCommand, CommandError
from backend.models import Category, Product, Shop

class Command(BaseCommand):
    help = 'Импорт товаров и категорий из shop1.yaml'

    def _load_yaml(self, file_path: str) -> dict:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    
    def _find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
        return None

    def handle(self, *args, **options):
        path_root = options.get('path_root', '/')
        yaml_filename = options.get('yaml_filename', 'shop1.yaml')

        yaml_path = self._find(yaml_filename, path_root)
        if not yaml_path:
            raise CommandError('Файл {} не найден в указанной директории: {}'.format(yaml_filename, path_root))

        data = self._load_yaml(yaml_path)

        shop_name = data.get('shop', 'Shop')
        categories_data = data.get('categories', [])
        goods_data = data.get('goods', [])

        # Импорт категорий и привязка магазинов к категориям
        for category_data in categories_data:
            
            cat_name = category_data.get('name')
            cat_id = category_data.get('id')
            cat_kwargs = {
                'id' : cat_id,
                'name' : cat_name,
            }
            category, _ = Category.objects.get_or_create(**cat_kwargs)

            for shop_data in category_data.get('shops', []):
                shop_name = shop_data.get('name')
                if not shop_name:
                    continue
                shop, _ = Shop.objects.get_or_create(name=shop_name)
                category.shops.add(shop)

        # Импорт товаров
        for good_data in goods_data:
            name = good_data.get('name')
            model = good_data.get('model')
            price = good_data.get('price')
            price_rrc = good_data.get('price_rrc')
            quantity = good_data.get('quantity')
            category_id = good_data.get('category')
            parameters = good_data.get('parameters')
            shop = Shop.objects.get(name=shop_name)
            category = Category.objects.get(id=category_id)

            product_kwargs = {
                'category': category, 
                'shop' : shop,
                'name': name,
                'price': price,
                'price_rrc': price_rrc,
                'quantity': quantity,
                'model': model,
                'parameters': parameters,
            }

            Product.objects.create(**product_kwargs)

        self.stdout.write(self.style.SUCCESS('Импорт завершен'))
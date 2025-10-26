import yaml
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from backend.models import (
    Shop, 
    Category,
    Product,
    ProductInfo,
    Parameter,
    ProductParameter,
)

from django.db import transaction

class Command(BaseCommand):
    help = 'Import products from YAML file into Shop/Categories/Products'

    def add_arguments(self, parser):
        parser.add_argument('yaml_path', type=str, help='Path to YAML file with shop data')

    @transaction.atomic
    def handle(self, *args, **options):
        yaml_path = Path(options['yaml_path'])
        if not yaml_path.exists():
            raise CommandError(f"YAML file not found: {yaml_path}")

        with yaml_path.open('r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Привязка магазина
        shop_name = data.get('shop')
        shop, _ = Shop.objects.get_or_create(name=shop_name)

        # Категории
        categories_map = {}
        for cat in data.get('categories', []):
            cat_obj, _ = Category.objects.get_or_create(name=cat['name'])

            if hasattr(cat_obj, 'shops'):
                cat_obj.shops.add(shop)
            categories_map[cat['id']] = cat_obj

        # Продукты
        for goods in data.get('goods', []):
            category_id = goods['category']
            category_obj = categories_map.get(category_id)

            product = Product.objects.create(
                name=goods['name'],
                category=category_obj
            )

            product_info = ProductInfo.objects.create(
                model=goods.get('model', ''),
                external_id=goods['id'],
                product=product,
                shop=shop,
                quantity=goods.get('quantity', 0),
                price=goods.get('price', 0),
                price_rrc=goods.get('price_rrc', 0)
            )

            # Параметры
            for param_name, param_value in goods.get('parameters', {}).items():
                parameter_obj, _ = Parameter.objects.get_or_create(name=param_name)

                ProductParameter.objects.create(
                    product_info=product_info,
                    parameter=parameter_obj,
                    value=str(param_value)
                )

        self.stdout.write(self.style.SUCCESS('Import completed successfully.'))
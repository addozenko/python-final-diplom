from ujson import loads as load_json

items_json = {'model': 'apple/iphone/xr', 'product': 'fewewkUUO', 'shop': 'Связной', 'quantity': '14', 'price': '110000', 'price_rrc': '116990', 'product_parameters': {'Диагональ (дюйм)': '6.5', 'Разрешение (пикс)': '2688x1242', 'Встроенная память (Гб)': '512', 'Цвет': 'золотистый'}}
items_json_str = str(items_json).replace("'", '"')

print(items_json_str)
items_dict = load_json(items_json_str)
print(type(items_dict))
#>uv run python practice_collections.py


# 1. Создаем словарь (анкету кофе)
latte = {"name": "Латте", "price": 250, "size": "XL"}

# 2. Безопасно достаем данные через .get()
# Если ключа "syrup" (сироп) нет, программа не упадет, а выведет "без сиропа"
syrup = latte.get("syrup", "без сиропа")
print(f"Ваш кофе: {latte['name']}, Сироп: {syrup}")

# 3. Делаем список из словарей (наше меню)
menu = [
	{"name": "Эспрессо", "price": 150},
	{"name": "Латте", "price": 250},
	{"name": "Капучино", "price": 200},
]

print("\n--- НАШЕ МЕНЮ ---")
# Перебираем список, где каждый элемент — это словарь item
for item in menu:
	print(f"Напиток: {item['name']} | Цена: {item['price']} руб.")

print("\n--- ЦЕНЫ СО СКИДКОЙ ---")
for item in menu:
    # Берем старую цену, вычитаем 50 и записываем обратно в этот же ключ 'price'
	item["price"] = item["price"] - 50
	print(f"Акция! {item['name']} теперь стоит всего {item['price']} руб.")

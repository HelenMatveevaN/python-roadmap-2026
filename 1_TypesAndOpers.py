# python3 less1.py

print("Числовые типы:")
#i: int = 42
#f: float = 3.14
#c: complex = 1 + 2j

big = 10 ** 100

print("\nDecimal — для денег:")
from decimal import Decimal

# ❌ Опасно
print(0.1 + 0.2)               # 0.30000000000000004

# ✅ Точно
print(Decimal("0.1") + Decimal("0.2"))   # 0.3

print("\nОператоры:")
a, b = 7, 3
print(a + b, a - b, a * b)
print(a / b)     # 2.333... (float division)
print(a // b)    # 2 (integer division)
print(a % b)     # 1
print(a ** b)    # 343

print("\nЦепочки сравнений:")
age = 25
if 18 <= age < 65:
    print("работоспособный возраст")

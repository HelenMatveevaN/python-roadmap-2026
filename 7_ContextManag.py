from contextlib import contextmanager, suppress
from time import perf_counter

class Database:
    def __enter__(self):
        print("[Database] connect")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[Database] disconnect")
        return False    # вернуть True — подавить исключение

    def query(self, sql: str):
        print(f"[Database] SQL: {sql}")

@contextmanager
def timer(label: str):
    start = perf_counter() # Выполняется при ВХОДЕ в `with`
    try:
        yield  # Пауза. Выполняется код внутри `with` (умирает в момент ошибки после with)
    finally:
        print(f"[Timer] {label}: {perf_counter() - start:.3f}s")

print("--- Старт программы ---\n")

print("1. Тестируем класс Database:")
with Database() as db:
    db.query("SELECT 1")

print("\n2. Тестируем функцию-таймер timer:")
with timer("sum_operation"):
    total = sum(range(10_000_000))

print("\n3. Тестируем встроенный suppress:")
with suppress(FileNotFoundError):
    open("not-exists.txt").read()
print("Исключение FileNotFoundError было успешно подавлено!")

print("\n--- Конец программы ---")

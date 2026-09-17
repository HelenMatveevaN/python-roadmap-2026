# табы в пробелы: uv run ruff check . --fix --unsafe-fixes



def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел."""
    return a + b


def greet(name: str, greeting: str = "Hello") -> str:
    """Приветствует пользователя."""
    return f"{greeting}, {name}!"


def total(*nums: float, scale: float = 1.0, **labels: str) -> float:
    """Считает сумму с масштабированием и выводит метаданные."""
    print(f"Словарь labels (kwargs): {labels}")
    return sum(nums) * scale


def counter():  # noqa: ANN201
    """Создает счетчик-замыкание."""
    n = 0

    def inc() -> int:
        nonlocal n
        n += 1
        return n

    return inc


def main() -> None:
    # 1. Базовое
    print(f"Сумма: {add(40, 2)}")

    # 2. Аргументы
    print(greet("Anna"))
    print(greet("Anna", greeting="Hi"))

    # 3. *args и **kwargs
    print(f"Результат total: {total(1, 2, 3, scale=2, source='api')}")

    # 4. Замыкание
    c = counter()
    print(f"Счетчик: {c()}, {c()}, {c()}")


if __name__ == "__main__":
    main()

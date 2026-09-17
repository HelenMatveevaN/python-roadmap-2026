def divide(a: float, b: float) -> float:
    """Безопасно делит два числа с демонстрацией всех блоков try-except."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("[except] Поймали деление на ноль!")
        return float("inf")
    except (TypeError, ValueError) as e:
        print(f"[except] Поймали ошибку типов: {e}. Пробрасываем дальше...")
        raise
    else:
        print("[else] Всё прошло отлично, ошибок нет.")
        return result
    finally:
        print("[finally] Чистка ресурсов: этот блок сработал ГАРАНТИРОВАННО.")


def main() -> None:
    print("=== СЦЕНАРИЙ 1: Успешное деление ===")
    print(f"Результат: {divide(10, 2)}\n")

    print("=== СЦЕНАРИЙ 2: Деление на ноль ===")
    print(f"Результат: {divide(10, 0)}\n")

    print("=== СЦЕНАРИЙ 3: Ошибка типов ===")
    try:
        # Передаем строку вместо числа
        print(f"Результат: {divide(10, 'два')}\n")  # type: ignore[arg-type]
    except TypeError:
        print("[main] Ошибка долетела до верхнего уровня и была поймана здесь.")


if __name__ == "__main__":
    main()

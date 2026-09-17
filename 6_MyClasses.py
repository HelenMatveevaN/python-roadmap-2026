class AppError(Exception):
    """Базовое исключение для нашего приложения."""


class NotFoundError(AppError):
    """Ошибка: объект не найден в системе."""


class ValidationError(AppError):
    """Ошибка валидации с детальной информацией о поле."""

    def __init__(self, field: str, reason: str) -> None:
        # Передаем понятный текст в базовый класс Exception
        super().__init__(f"Ошибка в поле '{field}': {reason}")
        self.field = field
        self.reason = reason


def main() -> None:
    print("=== ЧАСТЬ 1: Работа с кастомным классом ===")
    try:
        # Генерируем нашу умную ошибку
        raise ValidationError("user_id", "must be >= 0")
    except AppError as e:
        # Выводим имя класса ошибки и её текст
        print(f"Поймали класс: {type(e).__name__}")
        print(f"Текст ошибки: {e}")
        # Мы можем залезть внутрь объекта и достать атрибуты!
        if isinstance(e, ValidationError):
            print(f"Сломалось поле: {e.field}")

    print("\n=== ЧАСТЬ 2: Цепочка ошибок через raise ... from ===")
    try:
        int("abc")
    except ValueError as original_error:
        raise AppError("Критическая ошибка: неверный формат данных.") from original_error


if __name__ == "__main__":
    main()

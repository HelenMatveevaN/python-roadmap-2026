def make_logger(prefix: str):  # noqa: ANN201
    """Внешняя функция создаёт 'карман' для префикса (например, [INFO] или [ERROR])."""

    def logger(message: str) -> None:
        # Внутренняя функция навсегда запомнила свой prefix!
        print(f"{prefix} {message}")

    return logger


def main() -> None:
    # Создаём две независимые функции со своими скрытыми карманами
    info_log = make_logger("[INFO]")
    error_log = make_logger("[ERROR]")

    # Теперь используем их. Они помнят свой префикс!
    info_log("Сервер успешно запущен")
    info_log("Пользователь зашёл на сайт")
    error_log("База данных недоступна!")


if __name__ == "__main__":
    main()

def main() -> None:

    #Циклы
    print("1. Простой цикл range:")
    for i in range(5):
        print(i)

    # С индексом
    print("\n2. Цикл с индексом (enumerate):")
    for i, x in enumerate(["a", "b", "c"]):
        print(i, x)
        print(f"Индекс: {i}, Значение: {x}")

    # Параллельно
    print("\n3. Параллельный цикл (zip):")
    for name, age in zip(["A", "B"], [20, 30]):
        print(name, age)
        print(f"Имя: {name}, Возраст: {age}")


    # Проверяем разные типы событий
    # match/case
    print()
    print(handle({"type": "click", "x": 10, "y": 20}))  # click at (10,20)
    print(handle({"type": "key", "key": "a"}))         # letter A
    print(handle({"type": "key", "key": "5"}))         # non-letter key
    print(handle({"type": "move", "speed": 100}))       # unknown type=move, extra={'speed': 100}

    # Тестируем dataclass + match/case
    print()
    print("Проверка четвертей:")
    print(quadrant(Point(0, 0)))  # origin
    print(quadrant(Point(0, 5)))  # y-axis
    print(quadrant(Point(3, 4)))  # Q1
    print(quadrant(Point(-1, -2)))  # other

#match/case (3.10+)
def handle(event: dict) -> str:
    match event:
        case {"type": "click", "x": int(x), "y": int(y)}:
            return f"click at ({x},{y})"
        case {"type": "key", "key": str(k)} if k.isalpha():
            return f"letter {k.upper()}"
        case {"type": "key"}:
            return "non-letter key"
        case {"type": t, **rest}:
            return f"unknown type={t}, extra={rest}"
        case _:
            return "not an event"


#Сопоставление с dataclass
from dataclasses import dataclass


@dataclass
class Point: x: int; y: int

def quadrant(p: Point) -> str:
    match p:
        case Point(x=0, y=0): return "origin"
        case Point(x=0, y=_): return "y-axis"
        case Point(x=_, y=0): return "x-axis"
        case Point(x=x, y=y) if x > 0 and y > 0: return "Q1"
        case _: return "other"

if __name__ == "__main__":
    main()




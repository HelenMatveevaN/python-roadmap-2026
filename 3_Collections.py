def main() -> None:

    #Урок 3. Коллекции
    #list
    print("List:")
    xs: list[int] = [1, 2, 3]
    xs.append(4)            # [1, 2, 3, 4]
    xs.insert(0, 0)         # [0, 1, 2, 3, 4]
    xs.pop()                # [0, 1, 2, 3]     - удаляет последний
    xs.remove(2)            # [0, 1, 3]        - удаляет первое вхождение значения
    xs.sort()               # [0, 1, 3]
    xs.reverse()            # [3, 1, 0]

    # Срезы
    print("Срезы:")
    print(xs[1:4])      # [1, 0]          [старт : финиш : шаг]
    print(xs[::2])      # [3, 0]           каждый второй
    print(xs[::-1])     # [0, 1, 3]        реверс

    #tuple (Кортеж)
    point: tuple[int, int] = (3, 4)
    x, y = point        # распаковка
    print(f"\nРаспаковка кортежа: {x=}, {y=}")
    # tuple единственного элемента — обязательная запятая
    single = (42)
    print(f"Тип single: {type(single)}")
    single = (42,)
    print(f"Тип single: {type(single)}")

    #set (mutable) / frozenset (unmutable); (мн-во / заморож.мн-во)
    print()
    unique = {1, 2, 3}     # {1, 2, 3}
    unique.add(4)             # {1, 2, 3, 4}
    unique.discard(99)        # не упадёт если нет
    print(f"unique: {unique}")

    a, b = {1, 2, 3}, {2, 3, 4}
    print(f"Множества: пересечение={a & b}, объединение={a | b}, разность={a - b}")
    #print(a & b)              # пересечение: {2, 3}
    #print(a | b)              # объединение: {1, 2, 3, 4}
    #print(a - b)              # разность: {1}

    #dict
    user: dict[str, int] = {"id": 1, "age": 25}
    print(f"\nuser: {user}")
    print(f"Словари: id={user['id']}, name={user.get('name', 'default')}")

    print()
    for key, value in user.items():
        print(f"Ключ: {key}, Значение: {value}")

    # Объединение dict (3.9+)
    merged = {"a": 1} | {"b": 2}
    print(f"\nСлияние словарей: {merged}")

if __name__ == "__main__":
    main()

#Когда что использовать
#Нужно   Тип
#упорядоченная последовательность с изменениями  list
#фиксированная пара/тройка значений  tuple
#коллекция уникальных значений   set
#key → value dict
#ключ-композиция (frozen)    frozenset

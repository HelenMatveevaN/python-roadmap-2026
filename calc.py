"""calc.py — CLI-калькулятор.

Упражнение 1. CLI-калькулятор
Напиши calc.py:

Принимает выражение: python calc.py "2 + 2 * 3".
Операции: + - * / // %.
История в history.json (max 50 записей).
--history — последние 10.
--clear — очистка.
Использует match/case.
БЕЗ eval() и сторонних пакетов.

"""

#python3 calc.py
#python calc.py --clear
#python calc.py --history

from decimal import Decimal
from pathlib import Path

import os
import json
import sys
import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
}

prior_ops = ["*", "/", "//", "%"]
other_ops = ["+", "-"]

argument = sys.argv[1:]

file_name = "history.json"
history = []

match argument:
    case ["--clear"]:
        print("Очистка истории...")
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(history, f)

    case ["--history"]:
        print("Показ истории...")

        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    # Если файл поврежден, не падаем, а просто начинаем историю с чистого листа
                    history = []

        if history: # Если список НЕ пустой
            print(f"Ваша история вычислений:")
            for item in history[-10:]: # последние 10
                print(f" • {item}")
        else:
            print("История вычислений пуста.")


    case [expression]:
        print(f"Считаем выражение: {expression}")

        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    # Если файл поврежден, не падаем, а просто начинаем историю с чистого листа
                    history = []

        explist = expression.split() #get list

        if len(explist) < 3:
            print("Ошибка ввода выражения. \nПример ввода: python calc.py \"выражение\"")
            sys.exit()

        result = 0

        try: 
            while any(op in explist for op in prior_ops):
                indices = {op: explist.index(op) for op in prior_ops if op in explist}

                sign = min(indices, key=indices.get) #мин.оператор слева
                index = indices[sign]

                leftnum = Decimal(str(explist[index-1]))
                rightnum = Decimal(str(explist[index+1]))

                prior_func = OPS[sign]
                prior_result = prior_func(leftnum, rightnum)

                explist[index-1:index+2] = [prior_result]
                #print(f"explist = {explist}")

            while any(op in explist for op in other_ops):
                indices = {op: explist.index(op) for op in other_ops if op in explist}
                
                sign = min(indices, key=indices.get)
                index = indices[sign]

                leftnum = Decimal(str(explist[index-1]))
                rightnum = Decimal(str(explist[index+1]))

                other_func = OPS[sign]
                result = other_func(leftnum, rightnum)

                explist[index-1:index+2] = [result]
                #print(f"explist = {explist}")

            result = explist[0]
            print(f"Результат: {result}")

            history.append(f"{expression} = {result}")

            if len(history) > 50:
                del history[0]
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(history, f)
        
        except ZeroDivisionError:
            print("Ошибка: деление на ноль невозможно!")
            sys.exit()

        except ValueError:
            print("Ошибка: неверный формат чисел (например, ввели буквы вместо цифр)!")
            sys.exit()

        except Exception as e:
            # Этот блок поймает любую другую неизвестную ошибку
            print(f"Произошла непредвиденная ошибка: {e}")
            sys.exit()

    case _:
        print("Как пользоваться: python calc.py \"выражение\" или --history / --clear")
    

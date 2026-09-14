#Базовое
s = "Hello, World!"
print(len(s))         # 13
print(s.upper())
print(s.split(", "))  # ['Hello', 'World!']
print(s.replace("World", "Python"))

print()

#f-strings
name, age = "Anna", 30

print(f"{name} is {age} years old")
print(f"{name=}, {age=}")    # debug-форма
print(f"Сумма: {3 + 5}")

print()

#Форматирование
pi = 3.14159265

print(f"{pi:.2f}")         # 3.14
print(f"{pi:10.2f}")       # '      3.14'
print(f"{pi:_>10.2f}")     # '______3.14'
print(f"{1_000_000:_}")    # 1_000_000
print(f"{255:#x}")         # 0xff
print(f"{255:08b}")        # 11111111

print()

#bytes
b = "Привет".encode()
print(b.decode("utf-8"))   # Привет

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Ошибка: Деление на ноль!")
        return None
    else:
        div = x // y
        mod = x % y
        return div, mod

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = int(input("Введите номер пункта меню: "))
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
    result = divide(num1, num2)
    if result is not None:
        div, mod = result
        print("Частное:", div, ", Остаток:", mod)

else:
    print("Ошибка: Неправильно выбран пункт меню!")

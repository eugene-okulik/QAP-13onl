a = 7
b = int

while b != a:
    b = int(input('Введите число от 0 до 10: '))
    if b != a:
        print('Попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
print('Игра окончена :)')

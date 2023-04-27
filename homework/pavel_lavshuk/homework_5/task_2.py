a = 6
print('Попробуйте угадать число:')
while True:
    b = float(input())
    if b != a:
        print('попробуйте снова')
    if b == a:
        print('Поздравляю! Вы угадали!')
        break

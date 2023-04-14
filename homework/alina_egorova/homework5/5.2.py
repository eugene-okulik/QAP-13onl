# Угадайка
num = 15
user_num = int(input('Введите число: '))
while num != user_num:
    user_num = int(input('Поробуйте снова '))
print('Поздравляю! Вы угадали!')

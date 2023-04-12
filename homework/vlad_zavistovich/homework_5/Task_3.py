from random import randint


my_list = [randint(0, 100) for i in range(15)]

print('Список 15-ти рандомных чисел', my_list)  # В задании не было указано это распечатывать, но я вывел для проверки.
print('Максимальное число из рандомов =', max(my_list))
print('Минимальное число из рандомов =', min(my_list))
print('Сумма всех рандомов =', sum(my_list))
print('Среднее арифмитическое всех рандомов =', (sum(my_list) / len(my_list)))

# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел
# (каждое не меньше 0 и не больше 19).
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2,
# поскольку слово two в алфавите встречается позже слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)
import random

number_names = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

numbers_generator = [random.randint(0, 19) for i in range(random.randint(3, 100))]
user_numbers = ' '.join(map(str, numbers_generator))  # Некоторое количество чисел разделённых пробелом
listed_numbers = list(map(int, user_numbers.split(sep=' ')))
print(listed_numbers)
new_list = list(map(lambda element: number_names[element], listed_numbers))

new_list.sort()
print(new_list)
new_dict = {v: k for k, v in number_names.items()}
print(new_dict)
for i in new_list:
    print(new_dict[i], end=' ')

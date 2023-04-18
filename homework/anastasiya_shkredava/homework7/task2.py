# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел
# (каждое не меньше 0 и не больше 19). Выведите их через пробел в порядке лексикографического
# возрастания названий этих чисел в английском языке.


def check_numbers(numbers):
    while len(numbers) > 100:
        numbers = input('Вы ввели более 100 чисел. Введите не более ста чисел от 0 до 19 через пробел: ').split()

    out_of_range = [num for num in numbers if 0 > int(num) or int(num) > 19]
    if out_of_range:
        print(
            'Следующие числа будут отфильтрованы, потому что они меньше 0 или больше 19:' ', '.join(out_of_range)
        )
    return numbers


number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

user_numbers = input('Введите не более ста чисел от 0 до 19 через пробел: ').split()
user_numbers = check_numbers(user_numbers)
user_numbers_filtered = list(filter(lambda num: 0 <= int(num) <= 19, user_numbers))
user_numbers_ext = list(map(lambda num: [num, number_names[int(num)]], user_numbers_filtered))
sorted_user_numbers = list(map(lambda el: el[0], sorted(user_numbers_ext, key=lambda x: x[1])))
print('Результат сортировки порядке лексикографического возрастания названий:', ' '.join(sorted_user_numbers))

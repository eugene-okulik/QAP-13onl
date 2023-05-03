
numbers = list(map(int, input('Введите число через пробел от 0 и не более 100: ').split()))
number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}
user_numbers = list(filter(lambda num: 0 <= int(num) <= 19, numbers))
user_numbers = list(map(lambda num: [num, number_names[int(num)]], user_numbers))
sorted_user_numbers = list(map(lambda k: k[0], sorted(user_numbers, key=lambda x: x[1])))
print(f'Отсортированные числа {sorted_user_numbers}')

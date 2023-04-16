# Task №2

my_list = [int(num) for num in input('Enter numbers: ').split()]
my_list = list(filter(lambda num: 0 <= num <= 19, my_list))[:4]  # сначала фильтрует по величине, затем по длине
number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
new_dict = dict()
for key, value in number_names.items():
    new_dict[value] = key
new_list = list(map(lambda element: number_names[element], my_list))
new_list.sort()
for el in new_list:
    print(new_dict.get(el), end=' ')

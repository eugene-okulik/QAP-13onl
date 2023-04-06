my_dict = {
    'tuple': (1, 3, 5, 9, 10),
    'list': [5, 10, 15, 20, 45],
    'dict': {
        'name': 'Vlad',
        'surname': 'Zavistovich',
        'age': '25',
        'city': 'Warsaw',
        'country': 'Poland'
    },
    'set': {15, 19, 55, 78, 90},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'}

print(my_dict['tuple'][1:])  # Printed all the elements from the second to the end.

my_dict['list'].append(69)  # Added new element 69 to the end of the list.
my_dict['list'].pop(1)  # Deleted the second element from the list.

my_dict['dict']['i am a tuple'] = 'hello friend'  # Added new element with key 'i am a tuple'.
my_dict['dict'].pop('country')  # Deleted element 'country'

my_dict['set'].add(91)  # Added new element to the set.
my_dict['set'].remove(90)  # Deleted element '90'.

print(my_dict['str'][:8])  # Printed first 8 elements from the text.
print(my_dict['str'][35:39])  # Printed 4 elements from the middle of the text.
print(my_dict['str'][::3])  # Printed characters with indices that are multiples of three.
print(my_dict)  # Printed final version of the dictionary.

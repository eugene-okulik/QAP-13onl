import pprint


my_dict = {'tuple': ([1, 2, 3], ('Jun', 'Jul', 'Aug'), 1.234, True, '=)'),
           'list': [[1, 2, 3], ('Jun', 'Jul', 'Aug'), 1.234, False, '=)'],
           'dict': {'Belarus': ['Minsk', 'Grodno'], 1: True,
                    'numbers': [1, 2], (1, 2): ('one', 'two'), 'cat': '=^.^='},
           'set': {'hello', ('Jun', 'Jul', 'Aug'), 1.234, False, '=)'},
           'str': 'Mauris fringilla odio sit amet pretium ultricies. '
                  'Pellentesque habitant morbi tristique'}
print('Tuple elements starting from the 2nd:', my_dict['tuple'][1:])
my_dict['list'].append('one_more')
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = True
my_dict['dict'].pop((1, 2))
my_dict['set'].add(23)
my_dict['set'].remove(1.234)
print('The first 8 characters of the string:', my_dict['str'][:7])
mid = len(my_dict['str']) // 2
print('4 characters from the middle of the string:', my_dict['str'][mid - 2:mid + 2])
print('Characters with indices that are multiples of 3:', my_dict['str'][3::3])
pprint.pprint(my_dict, sort_dicts=False)

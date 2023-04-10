my_dict = {
    'tuple': (1, 2, 3, 4, 5,),
    'list': [5, 6, 7, 8, 9],
    'dict': {'key10': 10, 'key11': 11, 'key12': 12, 'key13': 13, 'key14': 14},
    'set': {15, 16, 17, 18, 19},
    'str': "Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristiqu"
}

print(my_dict['tuple'][1:])

my_dict['list'].append(101)
my_dict['list'].pop(1)

my_dict['dict']['i am tuple'] = 'tup'
my_dict['dict'].pop('key10')

my_dict['set'].add(999)
my_dict['set'].remove(15)

print(my_dict['str'][:7] + '\n', my_dict['str'][41:45] + '\n', my_dict['str'][::-3])

print(my_dict)

import random
print(random.random() * -1000000)
print(random.randint(0, 1000000))
print(random.randrange(0, 10, 3))
my_list = ['sdkjf', 'sdkjfs', 'sdfsd']

print(my_list[random.randrange(0, len(my_list))])
print(random.choice(my_list))
print(my_list)
my_list2 = my_list.copy()
print(my_list2)
my_list.pop(1)
print(my_list)
print(my_list2)

print('String' * 10)

lll = [1, 2, 20, 3, 10, 11, 12]
print(sorted(lll))
print(lll)
lll.sort()
print(lll)
print(max(my_list))

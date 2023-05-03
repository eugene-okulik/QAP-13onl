import random

my_dict = {1: 1, 2: 2, 3: 3, 4: 4}


def div_calc(a, b):
    if b == 1:
        my_dict[0]
    return a / b


for _ in range(20):
    try:
        print(div_calc(random.randrange(0, 5), random.randrange(-1, 5)))
    # except ZeroDivisionError as err:
    #     print(err.args)
    except KeyError:
        print('key')

# import import_me
from import_me import *
from homework.eugene_okulik.lesson_7.import7 import *
from homework.eugene_okulik.lesson_7 import *
from import_me import prettify, my_var, hello
from import_me import my_name_is_very_long_and_uncomfortable as short_name
from random import randint
import random
print(my_var)
print(my_var2)


hello()


@prettify
def calc(a, b):
    return a + b


calc(1, 2)

print(short_name(2))

print(random.choice([1, 3, 6, 7]))
print(randint(1, 5))

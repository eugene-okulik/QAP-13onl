def hello():
    print('hello')


my_var = 234
my_var2 = 4546


def my_name_is_very_long_and_uncomfortable(a):
    return a


def prettify(func):

    def wrapper(*args):
        print(args)  # print((1, 2))
        print(*args)  # print(1, 2)
        print('Summ of number is:')
        print(func(*args))  # func(1, 2)

    return wrapper

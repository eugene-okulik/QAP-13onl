def power(base, num=1):
    result = base ** num
    print(result)
    return result, 'finished'


f_result, text_result = power(2)
print(f_result, text_result)


def avg(*args: int):
    """
    Function counts average value
    """
    return sum(args) / len(args)


print(avg(1, 3, 6, 5, 8, 10, 34, 45))


def dictionary(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} is {v}')


dictionary(
    tree='slskdjf sldfsldkjsf',
    house='dkdkfjghdkjhs',
    sea='erterterter'
)


def my_func(var, arg: int = None, arg1=None):
    if arg:
        print('arg is defined')
        print(arg + 3)
    if arg1:
        print('arg1 is deifned')
    print(var)


my_func(3, arg1=2, arg=1)


def power1(base, num, a):
    result = base ** num
    print(result)
    return result, 'finished'


power1(num=3, base=2, a=5)

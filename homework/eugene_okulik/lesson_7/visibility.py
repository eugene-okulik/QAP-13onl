x = "Hello"


def say():
    global x
    x = "World"
    print(x)


say()
print(x)


text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer purus mauris, sagittis sed nisl sit amet,'
t = None


def parse(some_text: str):
    t = 3
    split_text = some_text.split()

    def print_text(element, symbol):
        global t
        t = 5
        print(t)
        print(f'{element} заканчивается на {symbol}')

    for x in split_text:
        if x.endswith('.'):
            print_text(x, 'точку')
        elif x.endswith(','):
            print_text(x, 'запятую')
        else:
            print_text(x, 'букву')
    print(t)


parse(text)
print(t)

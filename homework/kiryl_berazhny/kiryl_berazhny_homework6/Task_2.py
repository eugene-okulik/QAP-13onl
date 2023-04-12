# Задание 2 - "FuzzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print('Fuzz')
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    else:
        print(i)

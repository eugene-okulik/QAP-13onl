# Задание 2 - "FuzzBuzz"


fuzzbuzz = [
    'FuzzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fuzz' if num % 3 == 0
    else 'Buzz' if num % 5 == 0 else str(num) for num in range(1, 101)
]
print('\n'.join(fuzzbuzz))

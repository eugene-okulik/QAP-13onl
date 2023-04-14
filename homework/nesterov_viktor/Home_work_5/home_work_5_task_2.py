number = 5
guess = None

while guess != number:
    guess = int(input("Введите число от 1 до 10: "))
    if guess < number:
        print("Слишком мало, попробуйте снова.")
    elif guess > number:
        print("Слишком много, попробуйте снова.")
    else:
        print("Поздравляю! Вы угадали число.")

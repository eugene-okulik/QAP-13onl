user_answer = int(input("Guess the number\n"))
i = 9

while True:
    if i == user_answer:
        print("Congratulations!!! You guessed")
        break
    else:
        print("Wrong! Try again")
        user_answer = int(input("Guess the number\n"))

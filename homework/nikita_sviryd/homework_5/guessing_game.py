import random

rand_num = random.randrange(0, 9)
#print(rand_num)
while True:
    user_num = int(input("Угадайте цифру от 0 до 9: "))
    if user_num == rand_num:
        print("Поздравляю, вы угадали")
        break
    else:
        print("Попробуйте снова")

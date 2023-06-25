for posl in range(1, 101):
    if posl % 3 == 0 and posl % 5 == 0:
        print("FuzzBuzz")
    elif posl % 3 == 0:
        print("Fuzz")
    elif posl % 5 == 0:
        print("Buzz")
    else:
        print(posl)

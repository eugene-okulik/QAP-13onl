user_operation = input("Select the operation: 1.plus, 2.minus, 3.mult, 4.div\n")

user_first_num = int(input("Enter first number\n"))
user_second_num = int(input("Enter second number\n"))


def plus(x, y):
    return print(f"Sum =  {x + y}")


def minus(x, y):
    return print(f"Difference =  {x - y}")


def mult(x, y):
    return print(f"Product of numbers =  {x * y}")


def div(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Division by zero prohibited")
        result = f"Quotient of numbers =  {x / y}. Remainder of the division = {x // y}"
        return result
    except ZeroDivisionError as e:
        print(e)
        return None


if user_operation == '1':
    print(plus(user_first_num, user_second_num))

if user_operation == '2':
    print(minus(user_first_num, user_second_num))
    # print("Difference = " + str(minus(user_first_num, user_second_num)))

if user_operation == '3':
    print(mult(user_first_num, user_second_num))

if user_operation == '4':
    print(div(user_first_num, user_second_num))




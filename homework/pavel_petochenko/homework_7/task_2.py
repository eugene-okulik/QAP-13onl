# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19).
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке. Т.е.,
# скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в алфавите встречается позже слова
# three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)


number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}
name_numbers = {v: k for k, v in number_names.items()}


def convert_to_words(numbers_list):
    if not all(0 <= n <= 19 for n in numbers_list):
        raise ValueError("Введенные числа должны быть от 0 до 19 включительно.")
    if len(numbers_list) > 100:
        raise ValueError("Максимально допустимое количество введенных цифр - 100.")
    num_words = [name_numbers[name] for name in sorted(number_names[n] for n in numbers_list)]
    return num_words


try:
    num = input('Введите числа от 0 до 19: ').split()
    num = [int(n) for n in num]
    numbers = convert_to_words(num)
    print(" ".join(str(n) for n in numbers))
except ValueError as e:
    print("Error:", e)

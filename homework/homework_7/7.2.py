# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19). Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в алфавите встречается позже
# слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является
# истинным)

num = input('Введите числа: ').split()
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
nums = []
for i in num:
    nums.append(int(i))
nums_sorted = sorted(nums, key=lambda x: words[x])
new_nums = ''
for i in nums_sorted:
    new_nums += str(i) + ' '
print(new_nums)

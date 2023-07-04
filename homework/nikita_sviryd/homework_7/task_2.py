# 'что я сделал и как, сам не до конца понял, пользовался гуглом, наполовину списал, но сделал.'
#  + 'что-то с этим было сложно, потренируюсь отдельно на эту тему'
number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

numbers = input().split()
numbers = [int(x) for x in numbers]
number_names_list = [number_names[x] for x in numbers]
number_names_list.sort()

for name in number_names_list:
    number = list(number_names.keys())[list(number_names.values()).index(name)]
    print(number, end=' ')

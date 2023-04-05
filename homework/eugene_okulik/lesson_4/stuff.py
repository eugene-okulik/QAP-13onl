my_tuple = (7, 'text', False)
my_list = [3, 6, 7, 7, 'text', False]
# f_elt = my_tuple[0]
# s_elt = my_tuple[1]
# t_elt = my_tuple[2]
# f_elt, s_elt, t_elt = my_tuple
f_elt, s_elt, t_elt = my_list[:3]
print(s_elt)
print(my_list)
print(my_list[:4])
print(my_list[4:])
print(my_list[2:5])
print(my_list[1:5:2])
print(my_list[::2])
print(my_list[::-2])
print(my_list[-1])

my_text = 'my long text'
print(len(my_text))
print(my_text[3:7])
print('long' in my_text)
splitted_text = my_text.split()
print(splitted_text)
lipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vitae risus eu nibh aliquet posuere.'
split_lipsum = lipsum.split('. ')
print(split_lipsum)
products = 'roses, tulips, magnolia'
split_products = products.split(', ')
print(split_products)
new_list = ['roses', 'tulips', 'magnolia']
new_text = ', '.join(new_list)
print(new_text)

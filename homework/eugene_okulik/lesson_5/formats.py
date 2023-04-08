text2 = 'Спасибо, {1}, ваш заказ №{0}  оплачен'
name = 'Petia'
order = 1234
text = 'Спасибо, %s, ваш заказ №%s  оплачен'
print('Спасибо, ' + name + ', ваш заказ №' + str(order) + ' оплачен')
print(text % (order, name))

print(text2.format(order, name))

text3 = f'Спасибо, {name}, ваш заказ №{order}  оплачен'
print(text3)

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, ' \
       'facilisis vitae semper at, dignissim vitae libero'
my_list = text.split()
print(my_list)

for word in my_list:
    if ',' in word:
        word = word.replace(',', 'ing,')
        print(word, end=' ')
    elif '.' in word:
        word = word.replace('.', 'ing.')
        print(word, end=' ')
    else:
        word = f'{word}ing'
        print(word, end=' ')

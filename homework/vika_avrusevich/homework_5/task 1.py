# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
# в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит получившийся текст на экран.


string = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
         'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
new_list = string.split(' ')
print(new_list)

for word in new_list:
    if ',' in word:
        word = word.replace(',', 'ing,')
        print(word, end=' ')
    elif '.' in word:
        word = word.replace('.', 'ing.')
        print(word, end=' ')
    else:
        word = f'{word}ing'
        print(word, end=' ')


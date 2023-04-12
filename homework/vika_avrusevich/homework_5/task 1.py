# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

string = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
         'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
final_list = string.split(' ')
print(final_list)

for word in final_list:
    if ',' in word:
        word = word.replace(',', 'ing,')
        print(word, end=' ')
    elif '.' in word:
        word = word.replace('.', 'ing.')
        print(word, end=' ')
    else:
        print(f'{word}ing', end=' ')


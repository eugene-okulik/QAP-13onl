# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте “Etiam tincidunt neque erat,
# quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после этого
# выводит получившийся текст на экран.

my_text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, ' \
          'facilisis vitae semper at, dignissim vitae libero'
my_list = my_text.split()
print(my_list)
my_newlist = []
for word in my_list:
    if ',' in word:
        word = word.replace(",", "ing,")
        my_newlist.append(word)
    elif '.' in word:
        word = word.replace(".", "ing.")
        my_newlist.append(word)
    else:
        word = f'{word}ing'
        my_newlist.append(word)
print(' '.join(my_newlist))

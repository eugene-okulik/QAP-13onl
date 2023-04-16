# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

list_text = text.split()
empty_str = ''
print(list_text)
for word in list_text:
    if word.endswith(',') or word.endswith('.'):
        comma = word[-1]
        word = word[:-1]
        word = word + 'ing' + comma + ' '
        print(word)
        empty_str = empty_str + word
    else:
        word = word + 'ing'
        print(word)
        empty_str = empty_str + word + ' '
empty_str = empty_str[:-1]
print(empty_str)

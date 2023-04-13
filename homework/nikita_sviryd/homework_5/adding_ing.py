text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,' \
       ' facilisis vitae semper at, dignissim vitae libero'

words = text.split()

texting = ''
# Задумка, что проверяется есть ли в конце слова знак. если есть, то обрезаем знак,
# добавляем "ing" добавляем знак, добавляем пробел
for word in words:
    if word[-1] != ',' and word[-1] != '.':
        texting += word + 'ing '
    else:
        texting += word[:-1] + 'ing' + word[-1] + ' '


print(texting)

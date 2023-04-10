# добавление к каждому слову окончания ing

words = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = words.split()
for index in range(len(words)):
    if words[index][-1].isalnum():
        words[index] += 'ing'
    else:
        words[index] = words[index][:-1] + 'ing' + words[index][-1]
print(' '.join(words))


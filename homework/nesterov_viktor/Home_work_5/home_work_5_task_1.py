text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel." \
       " Integer urna nisl,facilisis vitae semper at, dignissim vitae libero"

# Разбиваем текст на отдельные слова
words = text.split()

# Проходим по каждому слову и добавляем 'ing'
for i in range(len(words)):
    words[i] = words[i] + "ing"

# Соединяем слова в единый текст
result = " ".join(words)

# Выводим полученный текст на экран
print(result)

# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте.


text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
text = text.split(' ')
edited_text = []
for el in text:
    if el.isalnum():
        el += 'ing'
    else:
        el = el[:-1] + 'ing' + el[-1:]
    edited_text.append(el)
edited_text = " ".join(edited_text)
print(edited_text)

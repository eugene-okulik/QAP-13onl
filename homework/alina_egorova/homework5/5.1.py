# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
text_list = text.split()
print(text_list)
new_text = ''
my_text = []
for my_text in text_list:
    if ',' in my_text:
        my_text = my_text.replace(',', 'ing, ')
        new_text += my_text
    if '.' in my_text:
        my_text = my_text.replace('.', 'ing. ')
        new_text += my_text
    if my_text[-5:] in my_text:
        if my_text[-5:] == 'ing, ' or my_text[-5:] == 'ing. ':
            continue
        my_text = my_text + 'ing '
        new_text += my_text
print(new_text)

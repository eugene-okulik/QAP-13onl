# Шифр Цезаря

user_text = input('Введите текст на русском языке: ')
step = int(input('Введите шаг: '))
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def cipher(text, shift):

    text = text.lower()
    new_text = str()
    for letter in text:
        if letter in alph:
            new_text += alph[(alph.find(letter) + shift) % len(alph)]
        else:
            new_text += letter
    return new_text


print(cipher(user_text, step))

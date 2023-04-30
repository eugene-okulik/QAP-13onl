# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.

print('Выберите операцию: \n'
      '1. Зашифровать \n'
      '2. Расшифровать \n')
enc_dec = input('Введите номер операции: ')
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
step = int(input('Введите шаг шифровки: '))
message = input("Введите текст для шифровки: ")
cipher = ''


def encode():
    global cipher
    for letter in message:
        letter_position = alphabet.find(letter)
        new_letter = letter_position + step
        if letter in alphabet:
            cipher = cipher + alphabet[new_letter]
        else:
            cipher = cipher + letter
    print(cipher)


def decode():
    global cipher
    for letter in message:
        letter_position = alphabet.find(letter)
        new_letter = letter_position - step
        if letter in alphabet:
            cipher = cipher + alphabet[new_letter]
        else:
            cipher = cipher + letter
    print(cipher)


match enc_dec:
    case '1':
        encode()
    case '2':
        decode()

# Эта программа шифрует и расшифровывает введенную пользователем строку на английском/русском языке и выводит результат.


alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def encode(text: str, shift: int, alphabet):
    """
    Эта функция шифрует текст пользователя.
    """
    encoded_text = ''
    for letter in text:
        if letter.isalpha():
            case = 'up' if letter.isupper() else 'low'
            position = alphabet.find(letter.lower()) + shift % len(alphabet)
            if alphabet.count(letter.lower()) != 0 and position < len(alphabet):
                letter = letter_case(case, alphabet, position)
            elif alphabet.count(letter.lower()) != 0 and position >= len(alphabet):
                position = position % len(alphabet)
                letter = letter_case(case, alphabet, position)
        else:
            letter = letter
        encoded_text += letter
    return print('Зашифрованный текст: ', encoded_text)


def decode(text: str, shift: int, alphabet):
    """
    Эта функция расшифровывает текст пользователя.
    """
    decoded_text = ''
    for letter in text:
        if letter.isalpha():
            case = 'up' if letter.isupper() else 'low'
            position = alphabet.find(letter.lower()) - shift % len(alphabet)
            if alphabet.count(letter.lower()) != 0:
                letter = letter_case(case, alphabet, position)
        else:
            letter = letter
        decoded_text += letter
    return print('Расшифрованный текст:', decoded_text)


def text_check(text, alphabet):
    """
    Эта функция проверяет, есть ли в тексте символы из алфавита языка, не выбранного пользователем.
    """
    for letter in text:
        if letter.isalpha() and alphabet.count(letter.lower()) == 0:
            return print(
                '*Ваш текст содержит буквы не русского алфавита, которые не будут зашифрованы.' if user_language == 2
                else '*Ваш текст содержит буквы не английского алфавита, которые не будут зашифрованы.'
            )


def letter_case(user_case, alphabet, letter_position):
    letter = alphabet[letter_position].upper() if user_case == 'up' else alphabet[letter_position].lower()
    return letter


user_language = int(input('Доступные языки:\n1. English\n2. Русский\n'
                          'Введите цифру, соответствующую языку, который вы хотите использовать для шифра:\n'))

while user_language > 2 or user_language < 1:
    user_language = int(input('Введенное число не соответствует какому-либо языку из списка. Попробуйте снова\n'))

user_alphabet = alphabet_en if user_language == 1 else alphabet_rus
user_text = input('Введите текст:\n')
text_check(user_text, user_alphabet)
user_shift = int(input('Введите значение сдвига:\n'))

print('\nВведенный вами текст:', user_text)
encode(user_text, user_shift, user_alphabet)
decode(user_text, user_shift, user_alphabet)

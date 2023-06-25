# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.

def encode(local_encoded_message, local_encoding_step):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    cipher = ''
    for letter in local_encoded_message:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            new_letter_position = (letter_position + local_encoding_step) % len(alphabet)
            cipher += alphabet[new_letter_position]
        else:
            cipher += letter
    return cipher


def decode(local_encoded_cipher, local_decoding_step):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    message = ''
    for letter in local_encoded_cipher:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            new_letter_position = (letter_position - local_decoding_step) % len(alphabet)
            message += alphabet[new_letter_position]
        else:
            message += letter
    return message


encoded_message = input("Введите текст для шифровки: ")
encoding_step = int(input("Введите шаг шифровки: "))

encrypted_message = encode(encoded_message, encoding_step)
print("Зашифрованный текст: ", encrypted_message)

decoding_step = encoding_step
decrypted_message = decode(encrypted_message, decoding_step)
print("Расшифрованный текст: ", decrypted_message)

# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.

text = input('Введите на русском текст который хотите зашифровать:\n')
shift_key = int(input('Введите ключ:\n'))


# Шифратор
def encode(encoding_value: str, shift_number: int):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    print(len(alphabet))
    alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ans = []
    for i in range(len(encoding_value)):
        if encoding_value[i] in alphabet:
            n = alphabet
        elif encoding_value[i] in alphabet_upper:
            n = alphabet_upper
        else:
            ans.append(encoding_value[i])
        if encoding_value[i] in n:
            for letter in range(len(n)):
                if letter + shift_number < len(n) and encoding_value[i] == n[letter]:
                    ans.append(n[letter + shift_number])
                    print(letter)
                elif letter + shift_number >= len(n) and encoding_value[i] == n[letter]:
                    ans.append(n[(0 + letter + shift_number) % len(n)])
                    print(letter)
                elif letter + shift_number < 0 and encoding_value[i] == n[letter]:
                    ans.append(n[(letter + shift_number) % len(n)])
                    print(letter)

    return ''.join(ans)


print(encode(text, shift_key))

text_decode = input('Введите на русском текст который хотите расшифровать:\n')
shift_key2 = int(input('Введите ключ:\n'))


# Дешифратор
def decode(decoding_value: str, shift_number: int):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ans = []
    for i in range(len(decoding_value)):
        if decoding_value[i] in alphabet:
            n = alphabet
        elif decoding_value[i] in alphabet_upper:
            n = alphabet_upper
        else:
            ans.append(decoding_value[i])
        if decoding_value[i] in n:
            for letter in range(len(n)):
                if letter - shift_number < len(n) and decoding_value[i] == n[letter]:
                    ans.append(n[letter - shift_number])
                elif letter - shift_number >= len(n) and decoding_value[i] == n[letter]:
                    ans.append(n[(1 - letter - shift_number) % (len(n) - 1)])
                elif letter - shift_number < 0 and decoding_value[i] == n[letter]:
                    ans.append(n[(letter - shift_number) % len(n)])

    return ''.join(ans)


print(decode(text_decode, shift_key2))

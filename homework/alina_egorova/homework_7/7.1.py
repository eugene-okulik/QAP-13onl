# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.
text = input("Введите текст, который хотите зашифровать: ")
shift = int(input("Укажите, с каким сдвигом шифровать текст: "))
lang = input("На каком языке введенный текст? (русский, английский): ")


def encode(text, shift, lang):
    result = []
    if lang.lower() == "русский" or lang.lower() == "russian":
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    elif lang.lower() == "английский" or lang.lower() == "english":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    else:
        return "Язык не поддерживается"
    for i in range(len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])
            index = (index + shift) % len(alphabet)
            result.append(alphabet[index])
        elif text[i] in alphabet.upper():
            index = alphabet.upper().index(text[i])
            index = (index + shift) % len(alphabet.upper())
            result.append(alphabet.upper()[index])
        else:
            result.append(text[i])
    return ''.join(result)


def decode(text, shift, lang):
    result = []
    if lang.lower() == "русский" or lang.lower() == "russian":
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    elif lang.lower() == "английский" or lang.lower() == "english":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    else:
        return "Язык не поддерживается"
    for i in range(len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])
            index = (index - shift) % len(alphabet)
            result.append(alphabet[index])
        elif text[i] in alphabet.upper():
            index = alphabet.upper().index(text[i])
            index = (index - shift) % len(alphabet.upper())
            result.append(alphabet.upper()[index])
        else:
            result.append(text[i])
    return ''.join(result)


encoded_text = encode(text, shift, lang)
print(encoded_text)
decoded_text = decode(encoded_text, shift, lang)
print(decoded_text)

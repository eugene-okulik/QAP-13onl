# Шифр Цезаря

my_text = input('Enter text: ')
step = int(input('Enter step: '))


def code(text, size):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    new_text = str()
    for index in range(len(text)):
        if text[index].isalnum():
            new_text += alphabet[(alphabet.find(text[index]) + size) % (len(alphabet))]
        else:
            new_text += text[index]
    return new_text


print(code(my_text, step))

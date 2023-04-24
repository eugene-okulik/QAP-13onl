print('Добро пожаловать в шифрование Цезаря')
some_text = str(input('Введите ваш текст: '))
step = int(input('Введите шаг: '))


def code(text, size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = str()
    for index in range(len(text)):
        if text[index].isalnum():
            new_text += alphabet[(alphabet.find(text[index]) + size) % (len(alphabet))]
        else:
            new_text += text[index]
    return new_text


print(code(some_text, step))

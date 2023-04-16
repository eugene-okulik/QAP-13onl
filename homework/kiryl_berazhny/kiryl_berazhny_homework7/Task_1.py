# Шифр Цезаря - написал функцию, которая работает в обе стороны (шаг положительынй и отрицательный).

my_text = input('Enter text: ')
step = int(input('Enter step: '))


def code(text, size):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    new_text = str()
    for index in range(len(text)):
        if text[index].isalnum():
            def en_de(alph, direction):
                if alph.find(text[index]) + direction % (len(alphabet) - 1) > (len(alphabet) - 1):
                    new_step = alph.find(text[index]) + direction % (len(alphabet) - 1) - len(alphabet)
                    return alph[new_step]
                else:
                    return alph[alph.find(text[index]) + direction % (len(alphabet) - 1)]
            if size >= 0:
                new_text += en_de(alphabet, size)
            else:
                new_text += en_de(alphabet[::-1], abs(size))
        else:
            new_text += text[index]
    return new_text


print(code(my_text, step))

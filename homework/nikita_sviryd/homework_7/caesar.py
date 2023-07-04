def encode(text, shift):
    text_new = ''
    for letter in text:
        if 96 < ord(letter) < 123:
            text_new += chr((ord(letter) - 97 + shift) % 26 + 97)
        elif 64 < ord(letter) < 91:
            text_new += chr((ord(letter) - 65 + shift) % 26 + 65)

        else:
            text_new += letter
    return text_new


def decode(text, shift):
    return encode(text, -shift)


print(encode('aazAAZ', 2))

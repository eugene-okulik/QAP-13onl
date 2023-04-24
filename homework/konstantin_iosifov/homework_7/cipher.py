def encode(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for t in text:
        if t not in alphabet:
            encrypted_text = encrypted_text + t
        else:
            position = alphabet.index(t)
            new_position = (position + shift) % len(alphabet)
            encrypted_symbol = alphabet[new_position]
            encrypted_text = encrypted_text + encrypted_symbol
    return encrypted_text


def decode(text, shift):
    return encode(text, -shift)


print(encode('hello world!', 3))

print(decode('khoor zruog!', 3))

print(encode('this is a test string', 5))

print(decode('ymnx nx f yjxy xywnsl', 5))

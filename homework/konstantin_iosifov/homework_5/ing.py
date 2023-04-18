import string

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
ending = 'ing'
text_list = text.split()

new_list = []

for t in text_list:
    if any(char in t for char in string.punctuation):
        new_list.append(t)
    else:
        new_list.append(t + 'ing')

result = " ".join(new_list)

print(result)

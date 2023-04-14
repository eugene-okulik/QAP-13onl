my_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper ' 
           'at, dignissim vitae libero')

my_text3 = my_text.split()
print(my_text3)
for word in my_text3:
    if word[-1] in [',', '.']:
        x = word[-1]
        my_text = ' '.join(my_text3)
        my_text2 = my_text.replace(',', '')
        my_text1 = my_text2.replace('.', '')
        my_text4 = my_text1.split()
        new_text = ' '.join(f'{word}ing' for word in my_text4)
        new_text2 = new_text.split()
# Так и не понял как добавить знаки пунктуации именно к тем словам в которых они были),если конечно все что выше
# правильно, хотелось бы подсказки).


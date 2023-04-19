my_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper '
           'at, dignissim vitae libero')

my_text1 = my_text.split()
new_text = ' '.join(f'{word}ing' for word in my_text1)
new_text1 = new_text.replace(',ing', 'ing,')
new_text2 = new_text1.replace('.ing', 'ing.')
print(new_text2)

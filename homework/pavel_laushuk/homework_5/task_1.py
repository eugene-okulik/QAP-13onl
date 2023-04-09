sentence = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
z = sentence.replace('', ",")
x = sentence.replace('.', '')
print(x)
x = sentence.split()
print(x)
# print(' '.join(sentence))
for name in x:
    # print(name, end = ' ')
    name = f'{name}ing'
    print(name)
# a = ['a', 'b', 'c']
# for i in a:
#     print(i,end = ' ')

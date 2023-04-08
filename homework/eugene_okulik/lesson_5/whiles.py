i = 0

while i < 0:
    print()
    i += 1

i = 0
while True:
    i += 1
    if i == 13:
        continue
    print(f'{i}. hello!')
    if i > 20:
        break

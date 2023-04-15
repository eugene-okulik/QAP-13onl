a = 255
b = 255
c = -258.1
d = -258.1

print(id(a), id(b), id(c), id(d))
print(hash(a), hash(b), hash(c), hash(d))
print(a is b)
print(a == b)
print(c is d)
print(c == d)

e = []
f = []
print(e is f)
print(e == f)

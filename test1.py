import copy

a = [1, 2, 3]
b = a.copy()
a.append(4)
print(b)
print(a)
b.append(8)
print(b)
print(a)
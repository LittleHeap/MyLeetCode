a = '99'
b = '99'

a = list(a)
b = list(b)

res = ''
while a and b:
    res = str(int(a.pop()) + int(b.pop())) + res

if a:
    a = ''.join(a)
    res = a + res
elif b:
    b = ''.join(b)
    res = b + res

print(res)
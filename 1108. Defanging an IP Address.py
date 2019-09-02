address = "255.100.50.0"

res = []
for a in address:
    if a == '.':
        res.append('[.]')
    else:
        res.append(a)

print(''.join(res))

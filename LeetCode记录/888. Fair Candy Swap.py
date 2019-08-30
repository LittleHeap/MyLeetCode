A = [1, 2, 5]
B = [2, 4]

a = {}
b = {}
sa = 0
sb = 0

for ele in A:
    a[ele] = 1
    sa = sa + ele
for ele in B:
    b[ele] = 1
    sb = sb + ele
target = abs(sa - sb) / 2

if sa > sb:
    for ele in B:
        if a.get(ele + target) is not None:
            print([int(ele + target), ele])
else:
    for ele in A:
        if b.get(ele + target) is not None:
            print([ele, int(ele + target)])

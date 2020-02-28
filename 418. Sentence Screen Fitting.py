rows = 2
cols = 3
sentence = ["t"]

n = len(sentence)
l = []
for ele in sentence:
    l.append(len(ele))

print(l)

res = 0
index = 0
start_row = None
start_res = None
zheng = None
bei = None

while rows > 0:
    print(zheng)
    print(bei)
    if zheng is not None:
        res += (rows // zheng) * bei
        rows = rows % zheng
        print(rows)
        zheng = None
    remain = cols
    if index == 0:
        start_row = rows
        start_res = res
    while remain >= l[index]:
        remain -= l[index] + 1
        index += 1
        if index == n:
            res += 1
            index = 0
            if remain < l[index]:
                zheng = start_row - rows + 1
                bei = res - start_res
    rows -= 1

print(res)


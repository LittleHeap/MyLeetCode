J = "z"
S = "ZZ"

jewel = {}
for j in J:
    jewel[j] = 1

num = 0
for s in S:
    if jewel.get(s) is not None:
        num = num + 1

print(num)
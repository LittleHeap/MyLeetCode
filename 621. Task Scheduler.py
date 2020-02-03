tasks = ["A", "A", "A", "B", "B", "B"]
n = 2



cul = {}
for ele in tasks:
    cul[ele] = cul.get(ele, 0) + 1

temp = sorted(cul.values())

print(temp)
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

d = {}
for i in range(len(start)):
    if start[i] != end[i]:
        d[i] = [start[i], end[i]]

print(d)



ratings = [1, 0,2]


lr = []

n = len(ratings)
for i in range(n):
    if i == 0:
        lr.append(1)
    else:
        if ratings[i] > ratings[i - 1]:
            lr.append(lr[i - 1] + 1)
        else:
            lr.append(1)


rl = lr
for i in range(n - 2, -1, -1):
    if ratings[i] > ratings[i + 1] and rl[i] <= rl[i + 1]:
        rl[i] = rl[i + 1] + 1

print(rl)
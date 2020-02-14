import bisect

T = [73, 74, 75, 71, 69, 72, 76, 73]

n = len(T)
stack = []
save = []

res = []

for i in range(n - 1, -1, -1):
    index = bisect.bisect_right(stack, T[i])
    if index == len(stack):
        res.append(0)
    else:
        res.append(save[index] - i)
    stack = stack[index:]
    save = save[index:]
    stack.insert(0, T[i])
    save.insert(0, i)


res.reverse()
print(res)


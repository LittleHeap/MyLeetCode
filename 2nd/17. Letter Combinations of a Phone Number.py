import copy

save = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

digits = '23'
n = len(digits)
res = []


def deep(cur, i):
    if i == n:
        res.append(cur)
        return
    else:
        for ele in save.get(int(digits[i])):
            newcur = copy.deepcopy(cur)
            newcur += ele
            deep(newcur, i + 1)


deep('', 0)
print(res)

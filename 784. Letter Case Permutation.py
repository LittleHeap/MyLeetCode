S = "CR"

res = []
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SL = list(S)
l = len(S)


def deep(SL, index):
    if index == l:
        res.append(''.join(SL))
        return
    for i in range(index, l):
        if SL[i] not in nums:
            c1 = SL.copy()
            c1[i] = c1[i].lower()
            deep(c1, index + 1)
            c2 = SL.copy()
            c2[i] = c2[i].upper()
            deep(c2, index + 1)
            break
        elif i == l - 1:
            res.append(''.join(SL))
        else:
            index = index + 1


deep(SL, 0)
print(res)

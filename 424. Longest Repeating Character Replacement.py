s = "AABA"
k = 0

d = {}
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = []
    d[s[i]].append(i)

print(d)

res = float('-inf')

for l in d.values():
    stack = []
    cur = []
    t = k
    for ele in l:
        if not stack:
            stack.append(ele)
        else:
            if ele == stack[-1] + 1:
                stack.append(ele)
            else:
                print(stack)
                while stack[-1] != ele - 1:
                    if t >= 1:
                        stack.append(stack[-1] + 1)
                        cur.append(stack[-1])
                        t -= 1
                    else:
                        stack.append(stack[-1] + 1)
                        cur.append(stack[-1])
                        index = stack.index(cur[0])
                        stack = stack[index + 1:]
                        cur.pop(0)
                stack.append(ele)
        res = max(res, len(stack) + t)



print(res)
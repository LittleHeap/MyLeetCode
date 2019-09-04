s = "{[]}"

d = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}
l = ['(', '[', '{']
r = [')', ']', '}']
pre = []

for ele in s:
    if ele in l:
        d[ele] = d.get(ele) + 1
        pre.append(ele)
    else:
        index = r.index(ele)
        if d.get(l[index]) > d.get(ele) and l.index(pre.pop()) == r.index(ele):
            # 注意验证和上一种左括号的匹配
            d[ele] = d.get(ele) + 1
        else:
            print(False)

for i in range(3):
    if d.get(l[i]) != d.get(r[i]):
        print(False)
print(True)

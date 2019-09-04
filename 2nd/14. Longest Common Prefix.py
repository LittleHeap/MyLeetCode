strs = ["dog", "racecar", "car"]

index = 0
ans = ''
flag = 0
while 1:
    cur = set()
    for ele in strs:
        if index == len(ele):
            flag = 1
            break
        else:
            cur.add(ele[index])
    if flag:
        break
    elif len(cur) > 1:
        break
    else:
        ans += cur.pop()
    index += 1

print(ans)

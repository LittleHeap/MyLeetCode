s = "abcd"
t = "abcde"

S = {}
for ele in s:
    S[ele] = S.get(ele, 0) + 1

for ele in t:
    if ele not in S:
        print(ele)
        break
    if S.get(ele) > 0:
        S[ele] = S.get(ele) - 1
    else:
        print(ele)

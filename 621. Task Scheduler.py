tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

have = [0 for i in range(26)]
all = 0

for ele in tasks:
    all = all + 1
    have[ord(ele) - 65] = have[ord(ele) - 65] + 1

have.sort()
have.reverse()
print(have)
print(all)
ans = 0

while all != 0:
    for i in range(n + 1):
        if have[i] > 0:
            have[i] = have[i] - 1
            all = all - 1
            ans = ans + 1
            if all == 0:
                print(ans)
                break
        else:
            ans = ans + 1
    have.sort()
    have.reverse()

print(ans)



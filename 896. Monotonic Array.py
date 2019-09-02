A = [1,1,1]

flag = set()
for i in range(1, len(A)):
    if A[i] == A[i - 1]:
        continue
    elif A[i] > A[i - 1]:
        flag.add(1)
    else:
        flag.add(0)
    if len(flag) == 2:
        print(False)
print(True)
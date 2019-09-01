A = [2, 2, 1]

A.sort()

if len(A) < 3:
    print(0)
else:
    for i in range(len(A) - 3, -1, -1):
        if A[i] + A[i + 1] > A[i + 2]:
            print(sum(A[i:i + 3]))
            break
    print(0)

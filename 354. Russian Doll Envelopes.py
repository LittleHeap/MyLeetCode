envelopes = [[28, 13], [23, 29], [44, 23], [31, 39], [15, 15], [6, 40], [36, 24], [37, 32], [15, 16], [27, 47], [16, 7],
             [31, 16], [12, 4], [12, 25], [36, 6], [31, 11], [43, 27], [37, 33], [43, 7], [45, 39], [38, 5], [14, 6],
             [22, 1], [19, 28], [49, 1], [15, 16], [39, 23], [47, 40], [1, 45], [33, 26], [3, 10], [18, 21], [38, 14],
             [23, 8], [37, 26], [12, 26], [40, 15], [10, 33]]

envelopes.sort()
print(envelopes)

n = len(envelopes)

dp = [1 for _ in range(n)]
res = 1

temp = [0, 0]
for i in range(n):
    temp = [0, 0]
    for j in range(i - 1, -1, -1):
        if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == res + 1:
                break
    res = max(res, dp[i])

print(dp)
print(max(dp))

[1, 1, 2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 1, 4, 6, 7, 5, 5, 6, 7, 7, 2, 7, 8, 8, 8, 2, 6, 7, 7, 3, 9, 8, 10, 11, 1]
[1, 1, 2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 1, 4, 6, 7, 5, 5, 6, 7, 7, 2, 7, 8, 8, 8, 2, 6, 7, 7, 3, 8, 8, 9, 10, 1]

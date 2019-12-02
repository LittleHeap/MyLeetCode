s1 = 'bird'
s2 = 'bertp'


def edit(s1, s2):
    n = len(s1)  # 4
    m = len(s2)  # 5
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    print(dp)
    i = m
    j = n
    res = []
    while i != 0 and j != 0:
        dir = [float('inf'), float('inf'), float('inf')]
        if s2[i - 1] == s1[j - 1]:
            res.append('None')
            i -= 1
            j -= 1
        else:
            if i - 1 >= 0:
                dir[2] = dp[i - 1][j]
            if j - 1 >= 0:
                dir[1] = dp[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                dir[0] = dp[i - 1][j - 1]
            choice = min(dir)
            index = dir.index(choice)
            if index == 0:
                res.append('Switch')
                i -= 1
                j -= 1
            elif index == 1:
                res.append('Add')
                j -= 1
            else:
                res.append('Delete')
                i -= 1
    res.reverse()
    return res


print(edit(s1, s2))

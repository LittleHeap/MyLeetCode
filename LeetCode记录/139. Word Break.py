s = "applepenappl"
wordDict = ["apple", "pen"]

wordDict = set(wordDict)
ans = set()

dp = [set() for _ in range(len(s) + 1)]
dp[0].add('')

for i in range(1, len(s) + 1):
    for ele in dp[i - 1]:
        if ele + s[i - 1] in wordDict:
            dp[i].add('')
            dp[i].add(ele + s[i - 1])
        else:
            dp[i].add(ele + s[i - 1])

if '' in dp[-1]:
    print(True)
else:
    print(False)

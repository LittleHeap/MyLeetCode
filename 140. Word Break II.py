class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def cup(word):
            return (len(word), word)

        hold = list(map(cup, wordDict))

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for index in range(len(s)):
            for step in hold:
                if index + 1 - step[0] >= 0 and dp[index + 1 - step[0]] == 1 and step[1] == s[index - step[
                    0] + 1:index + 1]:
                    dp[index + 1] = 1
        if dp[-1] == 0:
            return []

        res = []
        n = len(s)

        record = [[] for _ in range(len(s) + 1)]
        record[0].append([])
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1

        for index in range(len(s)):
            for step in hold:
                if index + 1 - step[0] >= 0 and dp[index + 1 - step[0]] == 1 and step[1] == s[index - step[
                    0] + 1:index + 1]:
                    dp[index + 1] = 1
                    for l in record[index + 1 - step[0]]:
                        newl = l.copy()
                        newl.append(step[1])
                        record[index + 1].append(newl)

        res = []
        for ele in record[-1]:
            res.append(' '.join(ele))
        return res

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        if not words:
            return 0

        d = {}
        dp = [1 for _ in range(len(words))]

        words = sorted(words, key=lambda x: len(x))

        for i, word in enumerate(words):
            d[word] = i

        for i, word in enumerate(words):
            for j in range(len(word)):
                cur = word[:j] + word[j + 1:]
                if cur in d and d[cur] < i:
                    dp[i] = max(dp[i], dp[d[cur]] + 1)

        return max(dp)
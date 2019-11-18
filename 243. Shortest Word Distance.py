class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1 = None
        w2 = None

        ans = float('inf')
        n = len(words)
        for i in range(n):
            if words[i] == word1:
                w1 = i
            if words[i] == word2:
                w2 = i
            if w1 is not None and w2 is not None:
                ans = min(ans, abs(w1 - w2))
        return ans
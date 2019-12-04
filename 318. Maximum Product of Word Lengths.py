class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = []
        n = len(words)

        for ele in words:
            l.append((set(list(ele)), len(ele)))

        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not l[i][0] & l[j][0]:
                    ans = max(ans, l[i][1] * l[j][1])
        return ans
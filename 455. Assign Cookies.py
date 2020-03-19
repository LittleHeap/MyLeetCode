class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        s.reverse()

        res = 0
        for i in range(len(g)):
            while s and s[-1] < g[i]:
                s.pop()
            if not s:
                break
            s.pop()
            res += 1

        return res








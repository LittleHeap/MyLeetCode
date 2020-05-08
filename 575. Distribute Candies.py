class Solution:
    def distributeCandies(self, c: List[int]) -> int:
        n = len(set(c))

        t = len(c) // 2

        return (t if n >= t else n)
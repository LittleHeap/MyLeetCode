class Solution:
    def shoppingOffers(self, p: List[int], offer: List[List[int]], n: List[int]) -> int:

        self.res = sum([n[i] * p[i] for i in range(len(n))])

        def deep(remain, now):
            self.res = min(self.res, now)
            for o in offer:
                newremain = [remain[i] - o[i] for i in range(len(n))]
                if min(newremain) >= 0:
                    newnow = now - sum([o[i] * p[i] for i in range(len(n))]) + o[-1]
                    deep(newremain, newnow)

        deep(n, self.res)

        return self.res
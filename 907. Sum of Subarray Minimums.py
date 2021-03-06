class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:

        res = 0
        stack = []
        d = {}

        for ele in A:
            cur = 1
            while stack and stack[-1][0] >= ele:
                cur += stack.pop()[1]
            stack.append((ele, cur))
            d[len(stack) - 1] = (d[len(stack) - 2] if len(stack) - 2 in d else 0) + ele * cur
            res += d[len(stack) - 1]

        return res % (10 ** 9 + 7)
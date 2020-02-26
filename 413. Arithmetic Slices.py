class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        cur = [A[0]]
        res = 0
        for i in range(1, len(A) - 1):
            if A[i] - A[i - 1] == A[i + 1] - A[i]:
                cur.append(A[i])
            else:
                cur.append(A[i])
                if len(cur) >= 3:
                    res += (1 + (len(cur) - 2)) * (len(cur) - 2) // 2
                cur = [A[i]]

        cur.append(A[-1])
        if len(cur) >= 3:
            res += (1 + (len(cur) - 2)) * (len(cur) - 2) // 2

        return res
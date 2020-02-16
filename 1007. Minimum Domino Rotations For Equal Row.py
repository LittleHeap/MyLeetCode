import collections

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        if len(A) == 1:
            return 0

        dA = collections.Counter(A)
        dB = collections.Counter(B)

        n = len(A)

        hold = []
        for ele in dA:
            if ele in dB and dA[ele] + dB[ele] >= n:
                hold.append(ele)

        res = float('inf')

        for ele in hold:
            k = 0
            for i in range(n):
                if A[i] == ele:
                    continue
                elif A[i] != ele and B[i] == ele:
                    k += 1
                else:
                    k = -1
                    break
            if k >= 0:
                res = min(res, k)
            k = 0
            for i in range(n):
                if B[i] == ele:
                    continue
                elif B[i] != ele and A[i] == ele:
                    k += 1
                else:
                    k = -1
                    break
            if k >= 0:
                res = min(res, k)

        if res == float('inf'):
            return -1
        else:
            return res



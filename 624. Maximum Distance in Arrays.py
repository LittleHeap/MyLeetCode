class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        cur = None
        res = float('-inf')
        for ele in arrays:
            if not ele:
                continue
            elif cur is None:
                cur = [ele[0], ele[-1]]
            else:
                res = max(abs(ele[0] - cur[1]), abs(ele[-1] - cur[0]), res)
                cur[0] = min(cur[0], ele[0])
                cur[1] = max(cur[1], ele[-1])

        return res
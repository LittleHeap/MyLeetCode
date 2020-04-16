class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur, res = set(), set()

        for ele in A:
            cur = {ele | j for j in cur} | {ele}
            res |= cur

        return len(res)
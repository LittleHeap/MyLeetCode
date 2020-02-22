class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        d = {}
        for ele in updates:
            d[tuple(ele)] = d.get(tuple(ele), 0) + 1

        res = [0 for _ in range(length)]

        for ele in d:
            for i in range(ele[0], ele[1] + 1):
                res[i] += ele[2] * d[tuple(ele)]

        return res
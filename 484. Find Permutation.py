class Solution:
    def findPermutation(self, s: str) -> List[int]:

        count = 0
        high = 2

        res = [1]

        for ele in s:
            if ele == 'D':
                count += 1
            else:
                if count != 0:
                    res += [j for j in range(high + count - 1, high - 1, -1)] + [res.pop()]
                    high += count
                    count = 0
                    res.append(high)
                    high += 1
                else:
                    res.append(high)
                    high += 1

        if count != 0:
            res += [j for j in range(high + count - 1, high - 1, -1)] + [res.pop()]

        return res
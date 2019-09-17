class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        have = set()
        have.add(tuple([0 for _ in range(n)]))
        cur = [0 for _ in range(n)]
        for i in range(2**n):
            index = n - 1
            for _ in range(n):
                cur[index] = 1 - cur[index]
                if tuple(cur) not in have:
                    have.add(tuple(cur))
                    new = ''
                    for ele in cur:
                        new += str(ele)
                    new = int(new, 2)
                    res.append(new)
                    break
                else:
                    cur[index] = 1 - cur[index]
                    index -= 1
        return res
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]

        res = []


        def deep(index, cur):
            s = sum(cur)
            for i in range(index, 9):
                if s + nums[i] == n and len(cur) == k - 1:
                    newcur = cur.copy()
                    newcur.append(nums[i])
                    res.append(newcur)
                    return
                elif s + nums[i] < n and len(cur) < k:
                    newcur = cur.copy()
                    newcur.append(nums[i])
                    deep(i + 1, newcur)
                else:
                    return


        deep(0, [])
        return res
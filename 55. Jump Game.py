class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        l = set()
        l.add(0)
        i = 0
        far = 0
        while l:
            if n - 1 in l:
                return True
            newl = set()
            for index in list(l):
                if index + nums[index] <= far:
                    l.remove(index)
                    continue
                for k in range(nums[index] + 1):
                    if index + k < n:
                        newl.add(index + k)
                        far = max(far, index + k)
            l = newl
            i += 1

        return False

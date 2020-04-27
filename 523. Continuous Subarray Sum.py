class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        d = {0: -1}

        sum = 0
        for i, ele in enumerate(nums):
            if k == 0:
                sum += ele
            else:
                sum = (sum + ele) % k
            if sum in d and i - d[sum] >= 2:
                return True
            elif sum not in d:
                d[sum] = i

        return False


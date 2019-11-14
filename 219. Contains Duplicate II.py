class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                if abs(d[nums[i]][-1] - i) <= k:
                    return True
                else:
                    d[nums[i]].append(i)
        return False
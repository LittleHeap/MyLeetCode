class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        ts = sum(nums)

        if ts % k != 0:
            return False

        tar = int(ts / k)

        mark = [False for _ in range(len(nums))]

        nums.sort(reverse=True)

        def deep(remain, k, idx):
            if k == 0:
                return True
            if remain == 0:
                return deep(tar, k - 1, 0)
            else:
                for i in range(idx, len(nums)):
                    if not mark[i] and nums[i] <= remain:
                        mark[i] = True
                        if deep(remain - nums[i], k, i + 1):
                            return True
                        mark[i] = False

        return deep(tar, k, 0)
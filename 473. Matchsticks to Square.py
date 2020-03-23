class Solution:
    def makesquare(self, nums: List[int]) -> bool:

        if not nums:
            return False

        target = sum(nums) / 4

        if int(target) != target:
            return False

        done = [False] * len(nums)

        def dfs(index, done, k, cur, target):
            if k == 1:
                return True
            if cur == target:
                return dfs(0, done, k - 1, 0, target)
            for i in range(index, len(nums)):
                if done[i] == False and cur + nums[i] <= target:
                    done[i] = True
                    if dfs(i + 1, done, k, cur + nums[i], target):
                        return True
                    done[i] = False
            return False

        return dfs(0, done, 4, 0, target)
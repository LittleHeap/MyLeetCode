class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        n = len(nums)

        step = [None for _ in range(n)]
        step[0] = 0

        target = n - 1

        far = 0
        flag = 0
        for i in range(n):
            if flag == 1:
                break
            if i + nums[i] <= far:
                continue
            for j in range(far + 1, i + 1 + nums[i]):
                if step[j] is None:
                    step[j] = step[i] + 1
                if j == target:
                    flag = 1
                    break
            far = i + nums[i]
        return step[j]

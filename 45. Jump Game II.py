class Solution:
    def jump(self, nums: List[int]) -> int:

        far = 0
        n = len(nums)
        if n == 1:
            return 0
        step = [0 for _ in range(n)]

        for i in range(n):
            curfar = i + nums[i]
            s = step[i] + 1
            for j in range(far + 1, curfar + 1):
                if j >= n - 1:
                    return s
                step[j] = s
                far = curfar
        return step[-1]
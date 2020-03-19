class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        hold = []
        if len(nums) < 3:
            return False

        temp = [None]

        m = nums[0]
        for i in range(1, len(nums)):
            temp.append(m)
            m = min(m, nums[i])

        hold.append(nums[-1])
        for i in range(len(nums) - 2, 0, -1):
            index = bisect.bisect_left(hold, nums[i])
            if index == 0 or temp[i] >= nums[i]:
                bisect.insort_left(hold, nums[i])
            else:
                pre = hold[index - 1]
                if temp[i] < pre:
                    return True
                else:
                    bisect.insort_left(hold, nums[i])

        return False
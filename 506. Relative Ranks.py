class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        hold = [(nums[i], i) for i in range(len(nums))]

        hold = sorted(hold, reverse=True)

        for i, (score, index) in enumerate(hold):
            if i == 0:
                nums[index] = "Gold Medal"
            elif i == 1:
                nums[index] = "Silver Medal"
            elif i == 2:
                nums[index] = "Bronze Medal"
            else:
                nums[index] = str(i + 1)

        return nums

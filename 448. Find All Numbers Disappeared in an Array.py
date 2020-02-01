class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        hold = set(nums)

        k = len(nums)
        res = []
        for i in range(1, k + 1):
            if i not in hold:
                res.append(i)

        return (res)
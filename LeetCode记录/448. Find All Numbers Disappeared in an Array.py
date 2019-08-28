class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        save = {}
        for ele in nums:
            save[ele] = 1
        res = []
        for i in range(len(nums)):
            if save.get(i + 1) is None:
                res.append(i + 1)
        return res

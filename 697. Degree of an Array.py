class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        save = {}
        index = {}

        s = 0
        num = None
        for i in range(len(nums)):
            save[nums[i]] = save.get(nums[i], 0) + 1
            s = max(s, save.get(nums[i]))
            if nums[i] not in index:
                index[nums[i]] = [i, i]
            else:
                index[nums[i]][1] = i

        hold = []
        for ele in save.items():
            if ele[1] == s:
                hold.append(ele[0])

        ans = float('inf')

        for ele in hold:
            ans = min(ans, index.get(ele)[1] - index.get(ele)[0])

        return ans + 1
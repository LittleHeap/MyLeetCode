class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        hold = {}

        for ele in nums:
            if not hold:
                hold[ele] = 1
                hold[-ele] = hold.get(-ele, 0) + 1
            else:
                newhold = {}
                for key in hold:
                    newhold[key + ele] = newhold.get(key + ele, 0) + hold[key]
                    newhold[key - ele] = newhold.get(key - ele, 0) + hold[key]
                hold = newhold

        return hold.get(S, 0)
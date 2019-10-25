class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        out = set()

        hold = set()

        for ele in nums:
            if ele not in out:
                if ele not in hold:
                    hold.add(ele)
                else:
                    hold.remove(ele)
                    out.add(ele)

        return list(hold)[0]
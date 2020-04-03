class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        d = defaultdict(int)
        c = collections.Counter(nums)

        for ele in nums:
            if d[ele - 1]:
                d[ele - 1] -= 1
            elif c[ele + 1] and c[ele + 2]:
                c[ele + 1] -= 1
                c[ele + 2] -= 1
            else:
                return False
            d[ele] += 1

        return True
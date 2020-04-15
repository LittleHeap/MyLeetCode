class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)

        hold = sorted(nums, key=functools.cmp_to_key(lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0),
                      reverse=True)

        return str(int(''.join(hold)))
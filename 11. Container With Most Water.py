class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        if len(height) < 2:
            return 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans

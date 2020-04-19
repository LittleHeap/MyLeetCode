class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:

        # Trick: solve the long increasing condition
        height.append(0)

        stack = []
        res = float('-inf')

        for i, ele in enumerate(height):
            temp = i
            while stack and stack[-1][0] >= ele:
                h, i = stack.pop()
                res = max(res, (temp - i) * h)
            stack.append((ele, i))

        return (0 if res == float('-inf') else res)
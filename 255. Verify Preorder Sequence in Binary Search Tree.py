class Solution:
    def verifyPreorder(self, p: List[int]) -> bool:

        stack = []

        down = float('-inf')

        for ele in p:
            if ele <= down:
                return False
            while stack and ele > stack[-1]:
                down = stack.pop()
            stack.append(ele)

        return True
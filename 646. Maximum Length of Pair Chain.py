class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()
        stack = []

        for ele in pairs:
            if not stack:
                stack.append(ele)
            elif ele[0] > stack[-1][1]:
                stack.append(ele)
            elif ele[1] < stack[-1][1]:
                stack[-1][1] = ele[1]

        return len(stack)
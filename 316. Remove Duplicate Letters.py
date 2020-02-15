class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)

        stack = []
        for i in range(len(s)):
            counter[s[i]] -= 1
            if s[i] not in stack:
                while stack and stack[-1] > s[i] and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(s[i])
        return ''.join(stack)
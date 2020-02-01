class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)

        nums = set()
        for i in range(10):
            nums.add(str(i))
        stack = []

        for char in s:
            if char == ']':
                cur = []
                while stack[-1] != '[':
                    cur.append(stack.pop())
                cur.reverse()
                stack.pop()
                times = []
                while stack and stack[-1] in nums:
                    times.append(stack.pop())
                times.reverse()
                times = int(''.join(times))
                for _ in range(times):
                    stack += cur
            else:
                stack.append(char)

        return ''.join(stack)
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []

        s = list(s)
        while s and s[0] == ')':
            s.pop(0)

        if not s:
            return 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            else:
                cur = []
                while stack and stack[-1] == 2:
                    cur.append(2)
                    stack.pop()
                if stack:
                    last = stack.pop()
                else:
                    stack = cur
                    stack.append(')')
                    continue
                if last == '(':
                    stack.append(2)
                    stack.extend(cur)
                else:
                    stack.append(')')
                    stack.extend(cur)
                    stack.append(')')

        res = 0
        cur = 0
        for i in range(len(stack)):
            if stack[i] == ')' or stack[i] == '(':
                cur = 0
            else:
                cur += 2
                res = max(res, cur)

        return res

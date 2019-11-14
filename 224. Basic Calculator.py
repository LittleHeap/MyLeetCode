class Solution:
    def calculate(self, s: str) -> int:
        nums = [str(i) for i in range(10)]
        nums = set(nums)
        S = s
        s = []
        l = len(S)
        i = 0
        while i < l:
            if S[i] in nums:
                r = i + 1
                cur = S[i]
                while r < l and S[r] in nums:
                    r += 1
                s.append(int(S[i:r]))
                i = r
            elif S[i] != ' ':
                s.append(S[i])
                i += 1
            else:
                i += 1
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                c = stack.pop()
                stack.pop()
                stack.append(c)
                c = stack.pop()
                while stack and (stack[-1] == '+' or stack[-1] == '-'):
                    if stack[-1] == '+':
                        stack.pop()
                        c = stack.pop() + int(c)
                    elif stack[-1] == '-':
                        stack.pop()
                        c = stack.pop() - int(c)
                stack.append(c)
            elif c == '+':
                stack.append(c)
            elif c == '-':
                stack.append(c)
            elif c != ' ':
                if stack and stack[-1] == '(':
                    stack.append(int(c))
                else:
                    while stack and (stack[-1] == '+' or stack[-1] == '-'):
                        if stack[-1] == '+':
                            stack.pop()
                            c = stack.pop() + int(c)
                        elif stack[-1] == '-':
                            stack.pop()
                            c = stack.pop() - int(c)
                    stack.append(int(c))
        return stack[0]

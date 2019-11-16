class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        nums = set([str(i) for i in range(0, 10)])
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] in nums:
                cur = ''
                while i < n and s[i] in nums:
                    cur += s[i]
                    i += 1
                stack.append(int(cur))
            else:
                stack.append(s[i])
                i += 1

        print(stack)
        n = len(stack)
        i = 0
        while i < n:
            if stack[i] == '*' or stack[i] == '/':
                if stack[i] == '*':
                    res = stack[i - 1] * stack[i + 1]
                    stack.pop(i - 1)
                    stack.pop(i - 1)
                    stack.pop(i - 1)
                    stack.insert(i - 1, res)
                    n -= 2
                else:
                    res = stack[i - 1] // stack[i + 1]
                    stack.pop(i - 1)
                    stack.pop(i - 1)
                    stack.pop(i - 1)
                    stack.insert(i - 1, res)
                    n -= 2
            else:
                i += 1

        new = []
        n = len(stack)
        i = 0
        while i < n:
            if i == 0:
                new.append(stack[i])
                i += 1
            elif stack[i] == '+':
                new.append(stack[i + 1])
                i += 2
            elif stack[i] == '-':
                new.append(-stack[i + 1])
                i += 2
            elif stack[i] == '*':
                new.append(new.pop() * stack[i + 1])
                i += 2
            elif stack[i] == '/':
                pre = new.pop()
                if pre < 0:
                    new.append(pre // stack[i + 1] + 1)
                else:
                    new.append(pre // stack[i + 1])
                i += 2
        return sum(new)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op = set()
        op.add('+')
        op.add('-')
        op.add('*')
        op.add('/')

        for ele in tokens:
            if ele not in op:
                stack.append(int(ele))
            else:
                a = stack.pop()
                b = stack.pop()
                if ele == '+':
                    stack.append(a + b)
                elif ele == '-':
                    stack.append(b - a)
                elif ele == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))

        return (int(stack[0]))

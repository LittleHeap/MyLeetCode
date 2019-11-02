class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op = set()
        op.add('+')
        op.add('-')
        op.add('*')
        op.add('/')

        cur = []
        for ele in tokens:
            if ele not in op:
                cur.append(int(ele))
            else:
                if ele == '+':
                    cur.append(cur.pop() + cur.pop())
                elif ele == '-':
                    a = cur.pop()
                    b = cur.pop()
                    cur.append(b - a)
                elif ele == '*':
                    cur.append(cur.pop() * cur.pop())
                else:
                    a = cur.pop()
                    b = cur.pop()
                    if b / a != b // a and b * a < 0:
                        res = b // a + 1
                    else:
                        res = b // a
                    cur.append(res)
        return cur[0]
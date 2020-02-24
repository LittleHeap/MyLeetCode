class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        res = ''

        if len(input.split('\n')) == 1 and '.' not in input:
            return 0
        elif len(input.split('\n')) == 1:
            return len(input)

        for ele in input.split('\n'):
            cur = ele.split('\t')
            if not stack:
                stack.append([len(cur) - 1, cur[-1]])
            else:
                if len(cur) - 1 == stack[-1][0]:
                    if '.' in stack[-1][1]:
                        new = ''
                        for t in stack:
                            new += t[1] + '/'
                        if len(new) - 1 > len(res):
                            res = new[:-1]
                    stack[-1] = [len(cur) - 1, cur[-1]]
                elif len(cur) - 1 > stack[-1][0]:
                    stack.append([len(cur) - 1, cur[-1]])
                else:
                    if '.' in stack[-1][1]:
                        new = ''
                        for t in stack:
                            new += t[1] + '/'
                        if len(new) - 1 > len(res):
                            res = new[:-1]
                    while stack and stack[-1][0] >= len(cur) - 1:
                        stack.pop()
                    stack.append([len(cur) - 1, cur[-1]])

        if '.' in stack[-1][1]:
            new = ''
            for t in stack:
                new += t[1] + '/'
            if len(new) - 1 > len(res):
                res = new[:-1]

        return len(res)
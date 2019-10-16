class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        path = path.split('/')

        for ele in path:
            if ele == '':
                continue
            elif ele == '.':
                continue
            elif ele == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ele)

        res = ''
        if stack:
            for ele in stack:
                res += '/' + ele
        else:
            res += '/'

        return res
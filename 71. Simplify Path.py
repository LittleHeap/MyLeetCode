class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        res = []

        for ele in path:
            if ele == '' or ele == '.':
                continue
            elif ele == '..':
                if res:
                    res.pop()
            else:
                res.append(ele)

        ans = '/'

        for ele in res:
            ans = ans + ele + '/'

        if len(ans) == 1:
            return '/'
        else:
            return ans[:-1]

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        res = []

        def deep(index):
            if index[-1] == n:
                ans = []
                print(index)
                for i in range(len(index)):
                    if i == 0:
                        continue
                    else:
                        ans.append(s[index[i - 1]: index[i]])
                res.append(ans)
                print(ans)
                return
            for i in range(index[-1] + 1, n + 1):
                now = list(s[index[-1]: i])
                temp = now.copy()
                temp.reverse()
                if now == temp:
                    newindex = index.copy()
                    newindex.append(i)
                    deep(newindex)

        deep([0])
        return res

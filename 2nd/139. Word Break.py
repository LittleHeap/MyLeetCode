class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        d = {}
        for ele in wordDict:
            d[ele] = len(ele)

        n = len(s)

        pre = set()
        pre.add(-1)

        for i in range(n):
            for ele in wordDict:
                if s[i - d.get(ele) + 1: i + 1] == ele and (i - d.get(ele)) in pre:
                    pre.add(i)
        return n - 1 in pre

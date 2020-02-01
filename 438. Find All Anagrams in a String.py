class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        for char in p:
            target[char] = target.get(char, 0) + 1

        k = len(p)

        cur = {}
        res = []
        for i in range(len(s)):
            if i < k:
                cur[s[i]] = cur.get(s[i], 0) + 1
                if cur == target:
                    res.append(i - k + 1)
            else:
                cur[s[i - k]] -= 1
                if cur[s[i - k]] == 0:
                    del cur[s[i - k]]
                cur[s[i]] = cur.get(s[i], 0) + 1
                if cur == target:
                    res.append(i - k + 1)

        return res
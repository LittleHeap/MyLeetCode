class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)

        for c in r:
            if c not in m  or  m[c] < r[c]:
                return False

        return True
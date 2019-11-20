class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = set()
        for ele in s:
            if ele in d:
                d.remove(ele)
            else:
                d.add(ele)
        if len(d) <= 1:
            return True
        else:
            return False
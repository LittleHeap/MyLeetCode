class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        res = []
        for ele in s:
            if (ord(ele) <= 122 and ord(ele) >= 97) or (ord(ele) <= 57 and ord(ele) >= 48):
                res.append(ele)

        temp = res.copy()
        temp.reverse()

        return temp == res

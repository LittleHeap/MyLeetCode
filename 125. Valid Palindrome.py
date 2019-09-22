class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        cur = []
        for ele in s:
            if (ord(ele) <= 57 and ord(ele) >= 48) or (ord(ele) <= 122 and ord(ele) >= 97):
                cur.append(ele)

        temp = cur.copy()
        temp.reverse()

        if temp == cur:
            return True
        else:
            return False

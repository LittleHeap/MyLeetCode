class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        an = x.copy()
        an.reverse()
        if x == an:
            return True
        else:
            return False

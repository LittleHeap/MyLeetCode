class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {}
        d[0] = 0
        d[1] = 1
        d[6] = 9
        d[8] = 8
        d[9] = 6
        n = len(num)
        l = 0
        r = n - 1
        while l <= r:
            if int(num[l]) not in d:
                return False
            else:
                if d[int(num[l])] == int(num[r]):
                    l += 1
                    r -= 1
                else:
                    return False
        return True
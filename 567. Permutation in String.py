class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if not s1:
            return True

        d = collections.Counter(s1)
        n = len(s1)

        stack = []

        for char in s2:
            if char in d:
                if d[char] >= 1:
                    d[char] -= 1
                else:
                    while d[char] < 1:
                        d[stack.pop(0)] += 1
                        n += 1
                    d[char] -= 1
                n -= 1
                stack.append(char)
                if n == 0:
                    return True
            else:
                while stack:
                    d[stack.pop(0)] += 1
                    n += 1
        return False
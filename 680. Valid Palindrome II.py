class Solution:
    def validPalindrome(self, s: str) -> bool:

        class Solution:
            def validPalindrome(self, s: str) -> bool:

                n = len(s)

                l, r = 0, n - 1

                flag = 1
                while l < r:
                    if s[l] != s[r]:
                        if flag:
                            l += 1
                            flag = 0
                        else:
                            break
                    else:
                        l += 1
                        r -= 1

                if l >= r:
                    return True

                l, r = 0, n - 1

                flag = 1
                while l < r:
                    if s[l] != s[r]:
                        if flag:
                            r -= 1
                            flag = 0
                        else:
                            break
                    else:
                        l += 1
                        r -= 1

                if l >= r:
                    return True

                return False



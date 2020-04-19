class Solution:
    def convertToBase7(self, n: int) -> str:

        def deep(num):
            if num < 0:
                return '-' + deep(-num)
            elif num < 7:
                return str(num)
            else:
                return deep(num // 7) + str(num % 7)

        return deep(n)
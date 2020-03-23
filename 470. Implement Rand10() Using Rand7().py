# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        while a > 5:
            a = rand7()
        b = rand7()
        while b == 7:
            b = rand7()
        if b % 2 == 1:
            return a
        else:
            return a + 5
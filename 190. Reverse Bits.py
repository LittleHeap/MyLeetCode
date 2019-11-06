class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        n = list(str(bin(n))[2:])
        l = len(n)
        for _ in range(32 - l):
            n.insert(0, '0')
        n.reverse()
        n = ''.join(n)
        n = int(n, 2)
        return n
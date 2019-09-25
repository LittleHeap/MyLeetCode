class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = list(bin(n))[2:]
        n.reverse()
        while len(n) < 32:
            n.append('0')
        n = int(''.join(n), 2)
        return n


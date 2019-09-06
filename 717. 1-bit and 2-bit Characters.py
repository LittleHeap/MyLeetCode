class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        bits.pop()

        i = 0
        while 1:
            if i == len(bits):
                return True
            if bits[i] == 1 and i + 1 == len(bits):
                return False
            elif bits[i] == 1:
                i += 2
            elif bits[i] == 0:
                i += 1

class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            num = str(hex(num))[2:]
        else:
            num = str(hex(num & 0xFFFFFFFF))[2:]
        return num
class Solution:
    def maximumSwap(self, num: int) -> int:

        num = list(str(num))

        a, b = 0, 0
        index = len(num) - 1

        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[index]:
                index = i
            elif num[i] < num[index]:
                a, b = i, index

        num[a], num[b] = num[b], num[a]
        return int(''.join(num))

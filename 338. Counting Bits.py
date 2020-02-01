class Solution:
    def countBits(self, num: int) -> List[int]:

        hold = [0]

        temp = 0
        target = 1

        for i in range(num):
            if i + 1 == target:
                hold.append(1)
                index = 1
                temp += 1
                target = 2 ** temp
            else:
                hold.append(hold[index] + 1)
                index += 1

        return hold
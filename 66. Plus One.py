class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        flag = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += flag
            if digits[i] == 10:
                digits[i] = 0
                flag = 1
            else:
                flag = 0
                break

        if flag:
            digits.insert(0, 1)
        return digits
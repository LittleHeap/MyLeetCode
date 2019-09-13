class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        flag = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1
            digits[i] += flag
            if digits[i] >= 10:
                digits[i] %= 10
                flag = 1
                if i == 0:
                    digits.insert(i, 1)
                    break
            else:
                break
        return digits

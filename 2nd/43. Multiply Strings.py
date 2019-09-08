class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        n1, n2 = 0, 0

        num1 = list(num1)
        num2 = list(num2)

        i = 0
        while num1:
            cur = num1.pop()
            n1 += num.get(cur) * (10 ** i)
            i += 1
        i = 0
        while num2:
            cur = num2.pop()
            n2 += num.get(cur) * (10 ** i)
            i += 1

        return str(n1 * n2)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = []

        a = 0
        b = 0

        for i in range(n):
            a += 1
            b += 1
            if a == 3 and b == 5:
                res.append('FizzBuzz')
                a = 0
                b = 0
            elif a == 3:
                res.append('Fizz')
                a = 0
            elif b == 5:
                res.append('Buzz')
                b = 0
            else:
                res.append(str(i + 1))

        return res

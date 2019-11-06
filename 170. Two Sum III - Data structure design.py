class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.d.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        self.d.sort()
        l = 0
        r = len(self.d) - 1
        while l < r:
            if self.d[l] + self.d[r] == value:
                return True
            elif self.d[l] + self.d[r] > value:
                r -= 1
                while r > l and self.d[r] == self.d[r + 1]:
                    r -= 1
            else:
                l += 1
                while l < r and self.d[l] == self.d[l - 1]:
                    l += 1
        return False

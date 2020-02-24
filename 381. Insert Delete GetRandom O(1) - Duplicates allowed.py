import numpy


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.all = 0
        self.move = 0
        self.l = []
        self.p = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.move = 1
        if val not in self.d:
            self.d[val] = 1
            self.all += 1
            return 1
        else:
            self.d[val] += 1
            self.all += 1
            return 0

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        self.move = 1
        if val in self.d:
            self.d[val] -= 1
            self.all -= 1
            if self.d[val] == 0:
                del self.d[val]
            return 1
        else:
            return 0

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.move == 0:
            return numpy.random.choice(self.l, p=self.p)

        self.l = []
        self.p = []
        for key in self.d:
            self.l.append(key)
            self.p.append(self.d[key] / self.all)
        self.move = 0

        return numpy.random.choice(self.l, p=self.p)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
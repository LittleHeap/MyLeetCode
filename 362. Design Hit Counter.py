class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.stack.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        temp = timestamp - 300
        while self.stack and self.stack[0] <= temp:
            self.stack.pop(0)
        return len(self.stack)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

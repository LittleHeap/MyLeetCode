class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.s = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        while self.l:
            if self.l[0][0] + 10 > timestamp:
                break
            else:
                self.s.remove(self.l[0][1])
                self.l.pop(0)

        if message in self.s:
            return 0
        else:
            self.l.append((timestamp, message))
            self.s.add(message)
            return 1

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
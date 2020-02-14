class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.s:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
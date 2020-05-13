class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q:
            self.q.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return (self.q[0] if self.q else -1)

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return (self.q[-1] if self.q else -1)

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return (True if not self.q else False)

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.q) == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
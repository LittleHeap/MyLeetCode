class LRUCache:

    def __init__(self, capacity: int):
        self.stack = []
        self.n = capacity
        self.save = {}

    def get(self, key: int) -> int:
        if self.save.get(key) is not None:
            self.stack.remove(key)
            self.stack.append(key)
            return self.save.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.save:
            self.stack.pop(self.stack.index(key))
            self.stack.append(key)
            self.save[key] = value
        elif len(self.stack) == self.n:
                self.stack.append(key)
                self.save.pop(self.stack.pop(0))
                self.save[key] = value
        else:
            self.stack.append(key)
            self.save[key] = value
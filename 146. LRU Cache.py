class LRUCache:

    def __init__(self, capacity: int):
        self.stack = []
        self.d = {}
        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            for i in range(len(self.stack)):
                if self.stack[i] == key:
                    self.stack.append(self.stack.pop(i))
                    return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            self.stack.append(key)
            self.d[key] = value
            if len(self.stack) > self.c:
                self.d.pop(self.stack.pop(0))
        else:
            self.d[key] = value
            i = self.stack.index(key)
            self.stack.append(self.stack.pop(i))

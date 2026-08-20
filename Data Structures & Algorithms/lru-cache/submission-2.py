class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cont = {}

    def get(self, key: int) -> int:
        if key in self.cont:
            val = self.cont.pop(key)
            self.cont[key] = val
            return self.cont[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cont:
            self.cont.pop(key)
            self.cont[key] = value
        else:      
            self.cont[key] = value

        if len(self.cont) > self.capacity:
            self.cont.pop(list(self.cont.keys())[0])
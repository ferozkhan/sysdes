from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)
        if self.capacity < len(self):
            self.popitem(last=False)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1

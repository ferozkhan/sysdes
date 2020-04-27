from collections import OrderedDict


class Slot:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def delete(self):
        if self.prev or self.next:
            key = self.key
            prev_node = self.prev
            next_node = self.next
            if next_node is not None and prev_node is not None:
                prev_node.next = next_node
                next_node.prev = prev_node
            elif prev_node is None:
                pass # ignore, head node
            elif next_node is None:
                prev_node.next = None
                self.prev = None
            return key


class Container:

    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied = 0
        self.head = None
        self.tail = None

    def delete_least_recent(self):
        new_tail = self.tail.prev
        deleted_key = self.tail.delete()
        self.tail = new_tail
        return deleted_key

    def make_recent(self, slot):
        if slot == self.head or self.head == self.tail:
            return
        elif slot == self.tail:
            self.tail = slot.prev
            self.tail.next = None
            slot.next = self.head
            self.head.prev = slot
            self.head = slot
        else:
            pass

    def _insert(self, slot):
        if self.head is None:
            self.head = slot
            self.tail = slot
        else:
            slot.next = self.head
            self.head.prev = slot
            self.head = slot
        self.occupied += 1

    def add_slot(self, slot):
        self._insert(slot)
        return slot

    def __repr__(self):
        return f'Container<capacity:{self.capacity}, occupied:{self.occupied}>'


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity
        super().__init__()

    def __getitem__(self, key):
        value = super().__getitem__(key)
        print(self)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.capacity:
            oldest = next(iter(self))
            del self[oldest]


lru = LRUCache(2)
lru[1] = 1
lru[2] = 2
# print(lru)
lru[1]
# print(lru)
lru[3] = 3
# print(lru)
    #
    # @property
    # def stats(self):
    #     return f"Capacity:\t{self.container.capacity}" \
    #            f"\nUsed:\t{self.container.occupied}"
    #
    # def _get(self, key):
    #     if key not in self.__cache:
    #         return -1
    #     slot = self.__cache[key]
    #     self.container.make_recent(slot)
    #     return slot.value
    #
    # def _put(self, key, value):
    #     self.__cache[key] = self.container.add_slot(Slot(key, value))
    #
    # def put(self, key, value):
    #     return self._put(key, value)
    #
    # def get(self, key):
    #     return self._get(key)


# cache = LRUCache(2)
#
# cache.put(1, 1)
# cache.put(2, 2)
# # assert 1 == cache.get(1)                # returns 1
# # cache.put(3, 3)                         # evicts key 2
# # assert -1 == cache.get(2)               # returns -1 (not found)
# print(cache.container.head.value, cache.container.tail.value)
# cache.put(4, 4)                         # evicts key 1
# print(cache.container.head.value, cache.container.tail.value)
# # assert -1 == cache.get(1)               # returns -1 (not found)
# # assert 3 == cache.get(3)                # returns 3
# # assert 4 == cache.get(4)                # returns 4

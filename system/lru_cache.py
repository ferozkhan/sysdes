

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkList:

    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def make_most_recent(self, node):
        if (self.head == node or
                self.head == self.tail):
            # ignore: if node is head, or list has only one node
            return

        if self.tail == node:
            self.tail = node.prev
            self.tail.next = None
            node.next = self.head
            self.head = node
            node.next.prev = self.head
        else:
            prev_node = node.prev
            next_node = node.next
            
            prev_node.next = next_node
            next_node.prev = prev_node
            head_node = self.head
            self.head = node
            self.head.next = head_node
            head_node.prev = self.head

    def delete(self):
        key = self.tail.key
        prev_node = self.tail.prev
        prev_node.next = None
        self.tail = prev_node
        self.count -= 1
        return key

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = {}
        self.list = DoubleLinkList()

    @property
    def slots(self):
        return self.list.count

    @property
    def most_recent(self):
        return self.list.head

    @property
    def least_recent(self):
        return self.list.tail

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self.list.make_most_recent(self._cache[key])
        return self._cache[key].val

    def put(self, key: int, val: int) -> None:
        if self.slots >= self.capacity:
            least_recent_key = self.list.delete()
            del self._cache[least_recent_key]

        self._cache[key] = Node(key, val)
        self.list.append(self._cache[key])
        self.list.make_most_recent(self._cache[key])


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
assert 1 == cache.get(1)                # returns 1
cache.put(3, 3)                         # evicts key 2
assert -1 == cache.get(2)               # returns -1 (not found)
cache.put(4, 4)                         # evicts key 1
assert -1 == cache.get(1)               # returns -1 (not found)
assert 3 == cache.get(3)                # returns 3
assert 4 == cache.get(4)                # returns 4

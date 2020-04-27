
class DLinkedList:
    def __init__(self) -> None:
        self.key = 0
        self.value = 0
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node) -> None:
        """ Always add node after head node"""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    @staticmethod
    def _remove_node(node) -> None:
        """ Always remove node before tail node"""
        _next = node.next
        _prev = node.prev

        _prev.next = _next
        _next.prev = _prev

    def _mode_to_head(self, node) -> None:
        """remove the node and add it to head"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> int:
        _node = self.tail.prev
        self._remove_node(_node)
        return _node.key

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node is None:
            return -1

        self._mode_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is None:
            new_node = DLinkedList()
            new_node.key = key
            new_node.value = value

            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail]
                self.size -= 1
        else:
            node.value = value
            self._mode_to_head(node)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
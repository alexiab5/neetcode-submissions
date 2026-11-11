class LRUCache:
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = None
        self.last = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self._move_to_end(node)
        return node.value

    def _move_to_end(self, node: Node) -> None:
        if node is self.last:
            return

        if node is self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

        self.last.next = node
        node.prev = self.last
        node.next = None
        self.last = node

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self._move_to_end(node)
            return

        if len(self.hashmap) == self.capacity:
            lru = self.head
            del self.hashmap[lru.key]
            
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.last = None

        new_node = self.Node(key, value)
        self.hashmap[key] = new_node

        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
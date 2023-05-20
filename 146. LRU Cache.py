class LinkedListNode:

    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkedListNode(-1, -1)
        self.tail = LinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove the node
            self.remove(node)
            # insert the node
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            # remove the node
            self.remove(node)
        if len(self.cache) == self.capacity:
            self.remove(self.tail.prev)
        # insert new node
        self.insert(LinkedListNode(key, value))

    def insert(self, node: LinkedListNode):
        self.cache[node.key] = node
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove(self, node: LinkedListNode):
        self.cache.pop(node.key)
        node.prev.next, node.next.prev = node.next, node.prev

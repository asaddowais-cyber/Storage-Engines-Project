
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class FastLRU:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.cache = {}

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_after_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert_after_head(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_after_head(node)
            return

        if len(self.cache) >= self.capacity:
            oldest = self.tail.prev
            self.remove(oldest)
            del self.cache[oldest.key]

        new_node = Node(key, value)
        self.insert_after_head(new_node)
        self.cache[key] = new_node


# Test the cache
my_cache = FastLRU(3)

my_cache.put("A", 1)
my_cache.put("B", 2)
my_cache.put("C", 3)

print(my_cache.get("A"))

my_cache.put("D", 4)

print(my_cache.get("B"))

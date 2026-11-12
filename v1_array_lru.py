
class ArrayLRU:

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.cache = []

    def get(self, key):
        for item in self.cache:
            if item[0] == key:
                self.cache.remove(item)
                self.cache.append(item)
                return item[1]

        return -1

    def put(self, key, value):
        for item in self.cache:
            if item[0] == key:
                self.cache.remove(item)
                break

        if len(self.cache) >= self.capacity:
            self.cache.pop(0)

        self.cache.append((key, value))


# Test the cache
my_cache = ArrayLRU(3)

my_cache.put("A", 1)
my_cache.put("B", 2)
my_cache.put("C", 3)

print(my_cache.cache)

print(my_cache.get("A"))
print(my_cache.cache)

my_cache.put("D", 4)
print(my_cache.cache)

print(my_cache.get("B"))

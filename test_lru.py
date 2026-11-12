
import random
from v1_array_lru import ArrayLRU
from v2_fast_lru import FastLRU

random.seed(42)

v1 = ArrayLRU(100)
v2 = FastLRU(100)

# Do 20,000 random operations
for i in range(20000):
    key = random.randint(1, 200)

    if random.randint(0, 1) == 0:
        value = random.randint(1, 1000)

        v1.put(key, value)
        v2.put(key, value)

    else:
        answer1 = v1.get(key)
        answer2 = v2.get(key)

        assert answer1 == answer2

    # Check the items in V2
    v2_items = []
    node = v2.tail.prev

    while node != v2.head:
        assert node.prev.next is node
        assert node.next.prev is node
        assert v2.cache[node.key] is node

        v2_items.append((node.key, node.value))
        node = node.prev
        assert len(v2_items) <= 100

    # Check that both caches are the same
    assert v1.cache == v2_items
    assert len(v2.cache) == len(v2_items)

print("All 20,000 operations passed!")

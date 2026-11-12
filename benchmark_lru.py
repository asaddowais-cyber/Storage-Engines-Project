
import random
import time

from v1_array_lru import ArrayLRU
from v2_fast_lru import FastLRU


capacities = [32, 128, 512, 2048, 8192]


for capacity in capacities:

    random.seed(42)
    operations = []

    # Create 100,000 random operations
    for i in range(100000):
        key = random.randint(1, capacity * 2)

        if random.randint(0, 1) == 0:
            value = random.randint(1, 1000)
            operations.append(("put", key, value))
        else:
            operations.append(("get", key, 0))

    # Create V1 and V2
    v1 = ArrayLRU(capacity)
    v2 = FastLRU(capacity)

    # Fill both caches before testing
    for key in range(1, capacity + 1):
        v1.put(key, key)
        v2.put(key, key)

    # Measure V1 speed
    start = time.perf_counter()

    for action, key, value in operations:
        if action == "put":
            v1.put(key, value)
        else:
            v1.get(key)

    time1 = time.perf_counter() - start

    # Measure V2 speed
    start = time.perf_counter()

    for action, key, value in operations:
        if action == "put":
            v2.put(key, value)
        else:
            v2.get(key)

    time2 = time.perf_counter() - start

    # Calculate operations per second
    speed1 = 100000 / time1
    speed2 = 100000 / time2

    # Print results
    print("Capacity:", capacity)
    print("V1 time:", round(time1, 3), "seconds")
    print("V2 time:", round(time2, 3), "seconds")
    print("V1 speed:", round(speed1), "ops/sec")
    print("V2 speed:", round(speed2), "ops/sec")
    print("------------------------")

print("All performance tests completed!")
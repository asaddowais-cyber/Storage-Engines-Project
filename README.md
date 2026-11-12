# Storage Engines Project

## LRU Cache Implementation

This project contains two implementations of an LRU (Least Recently Used) cache using Python.

- V1 Array LRU: Uses a Python list. Operations take O(C) time in the worst case.
- V2 Fast LRU: Uses a dictionary and doubly linked list. Operations take O(1) time on average.

## Testing

- `test_lru.py` runs 20,000 random operations to compare V1 and V2.
- `benchmark_lru.py` runs 100,000 operations per cache capacity to measure performance.
- Capacities tested: 32, 128, 512, 2048, and 8192.

## Results

V2 maintains much better performance as cache capacity increases, while V1 becomes slower.

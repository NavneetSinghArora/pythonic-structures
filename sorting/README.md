# Sorting Algorithms

## Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Performance Analysis
Worst case time complexity: O(n^2)
Average case time complexity: O(n^2)
Best case time complexity: O(n)
Space complexity: O(1)

The bubble sort algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n^2), where n is the number of items being sorted.
It is best used for small data sets or for educational purposes.
The algorithm is created using python with generator functions to yield the sorted array at each step.

### Implementation

This implementation of bubble sort algorithm is created using python with generator functions to yield the sorted array at each step. After each step, the array is printed to the console.
Also using a timer decorator to measure the time taken by the algorithm.


<!-- BENCHMARK_SORTING_START -->

### 📊 Sorting Benchmarks

| Algorithm | Mean | Min | Max | Std Dev | Ops/s | Rounds |
|-----------|------|-----|-----|---------|-------|--------|
| Native Sort | 249.63 ns | 220.24 ns | 3.56 µs | 31.36 ns | 4.01M ops/s | 195,122 |
| Bubble Sort | 16.37 µs | 15.38 µs | 799.38 µs | 8.39 µs | 61.08K ops/s | 9,150 |

<!-- BENCHMARK_SORTING_END -->
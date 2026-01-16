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
| Native Sort | 186.26 ns | 163.34 ns | 825.83 ns | 18.31 ns | 5.37M ops/s | 54,544 |
| Bubble Sort | 9.08 µs | 8.62 µs | 49.71 µs | 1.06 µs | 110.15K ops/s | 8,857 |

<!-- BENCHMARK_SORTING_END -->
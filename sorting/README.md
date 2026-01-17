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

## Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### Performance Analysis
Worst case time complexity: O(n^2)
Average case time complexity: O(n^2)
Best case time complexity: O(n)
Space complexity: O(1)

The insertion sort algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n^2), where n is the number of items being sorted.
It is best used for small data sets or for educational purposes.

### Implementation

This implementation of insertion sort algorithm is created using python with generator functions to yield the sorted array at each step. After each step, the array is printed to the console.
Also using a timer decorator to measure the time taken by the algorithm.


<!-- BENCHMARK_START -->

## 📊 Benchmark Results

### System Information

- **CPU**: Apple M4
- **Architecture**: arm64
- **Python**: 3.14.2
- **OS**: Darwin 25.2.0

### Sorting Algorithms

| Algorithm | Mean | Min | Max | Std Dev | Ops/s | Rounds |
|-----------|------|-----|-----|---------|-------|--------|
| Native Sort | 260.90 ns | 228.05 ns | 3.66 µs | 32.68 ns | 3.83M ops/s | 195,123 |
| Bubble Sort | 15.89 µs | 15.04 µs | 682.25 µs | 7.17 µs | 62.93K ops/s | 9,026 |
| Insertion Sort | 52.67 µs | 49.33 µs | 503.79 µs | 6.88 µs | 18.99K ops/s | 13,023 |

<!-- BENCHMARK_END -->
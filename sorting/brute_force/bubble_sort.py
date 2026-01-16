# This the implementation of bubble sort algorithm
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
# Time complexity: O(n^2)
# Space complexity: O(1)

# Problem Statement: Sort an array of integers in ascending order using bubble sort algorithm
# N = length of the array
# -500 <= ar[i] <= 500


import random
import time
from typing import Iterator, Tuple
from functools import wraps

# Creating a decorator to measure the time taken by a function
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time}")
        return result
    return wrapper

# Visualising the bubble sort algorithm
@timer
def visualise_bubble_sort(balance: list[int], sleep_time: int = 1) -> Tuple[int, list[int]]:
    print("Initial array:", balance)
    
    steps = 0
    sorted_balance = balance
    
    for _balance in execute_bubble_sort(balance):
        steps += 1
        sorted_balance = _balance

        # Adding a delay to visualise the sorting after every iteration
        time.sleep(sleep_time)
        print(f"Step {steps}: {_balance}")
    
    print(f"Sorting Complteted in {steps} steps")
    return steps, sorted_balance

# Executing the bubble sort algorithm as a generator and yielding the sorted array at each step
def execute_bubble_sort(balance: list[int]) -> Iterator[list[int]]:
    # Executing the bubble sort algorithm
    for i in range(len(balance)):
        swapped = False 
        for j in range(i + 1, len(balance)):
            if balance[j] < balance[i]:
                # Swapping the elements
                balance[j], balance[i] = balance[i], balance[j]
                swapped = True
        
        if not swapped:
            break

        # Yielding the sorted array at each step
        yield balance   

if __name__ == "__main__":
    balance = [random.randint(-500, 500) for _ in range(16)]
    visualise_bubble_sort(balance)
    
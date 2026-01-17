# This the implementation of bubble sort algorithm
# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
# Time complexity: O(n^2)
# Space complexity: O(1)

# Problem Statement: Sort an array of integers in ascending order using bubble sort algorithm
# N = length of the array
# -500 <= ar[i] <= 500


import time
from typing import Iterator, Tuple
from sorting.helpers import create_random_list
from utils.decorators import timer

# Visualising the bubble sort algorithm
@timer
def visualise_bubble_sort(balance: list[int], sleep_time: int = 1) -> Tuple[int, list[int]]:
    """
    Visualising the bubble sort algorithm
    
    Args:
        balance (list[int]): The list of integers to be sorted
        sleep_time (int, optional): The time to sleep between steps. Defaults to 1.
    
    Returns:
        Tuple[int, list[int]]: The number of steps and the sorted array
    """
    print("Initial array:", balance)
    
    steps = 0
    sorted_balance = balance
    
    # Using the generator to visualise the sorting by yielding the sorted array at each step
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
    """
    Executing the bubble sort algorithm as a generator and yielding the sorted array at each step

    Args:
        balance (list[int]): The list of integers to be sorted
    
    Returns:
        Iterator[list[int]]: The sorted array at each step
    """
    # Executing the bubble sort algorithm
    for i in range(len(balance)):
        swapped = False 
        for j in range(i + 1, len(balance)):
            if balance[j] < balance[i]:
                # Swapping the elements
                balance[j], balance[i] = balance[i], balance[j]
                swapped = True
        
        # If no elements were swapped, the array is already sorted. Hence break the loop
        if not swapped:
            break

        # Yielding the sorted array at each step
        yield balance   

if __name__ == "__main__":
    # Calling the helper function to create a random list
    balance = create_random_list(5)
    
    # Visualising the bubble sort algorithm
    visualise_bubble_sort(balance)
    
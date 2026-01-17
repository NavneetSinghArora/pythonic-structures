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
def visualise_bubble_sort(unsorted_list: list[int], sleep_time: int = 1) -> Tuple[int, list[int]]:
    """
    Visualising the bubble sort algorithm
    
    Args:
        unsorted_list (list[int]): The list of integers to be sorted
        sleep_time (int, optional): The time to sleep between steps. Defaults to 1.
    
    Returns:
        Tuple[int, list[int]]: The number of steps and the sorted array
    """
    print("Initial array:", unsorted_list)
    
    steps = 0
    sorted_list = unsorted_list
    
    # Using the generator to visualise the sorting by yielding the sorted array at each step
    for _sorted_list in execute_bubble_sort(unsorted_list):
        steps += 1
        sorted_list = _sorted_list

        # Adding a delay to visualise the sorting after every iteration
        time.sleep(sleep_time)
        print(f"Step {steps}: {_sorted_list}")
    
    print(f"Sorting Complteted in {steps} steps")
    print("Final Sorted List:", sorted_list)
    return steps, sorted_list

# Executing the bubble sort algorithm as a generator and yielding the sorted array at each step
def execute_bubble_sort(unsorted_list: list[int]) -> Iterator[list[int]]:
    """
    Executing the bubble sort algorithm as a generator and yielding the sorted array at each step

    Args:
        unsorted_list (list[int]): The list of integers to be sorted
    
    Returns:
        Iterator[list[int]]: The sorted array at each step
    """
    # Executing the bubble sort algorithm
    for i in range(len(unsorted_list)):
        swapped = False 
        for j in range(0, len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swapping the elements
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        
        # Yielding the partially / fully sorted array at each step
        yield unsorted_list   

        # If no elements were swapped, the array is already sorted. Hence break the loop
        if not swapped:
            break

if __name__ == "__main__":
    # Calling the helper function to create a random list
    unsorted_list = create_random_list(5)
    
    # Visualising the bubble sort algorithm
    visualise_bubble_sort(unsorted_list)
    
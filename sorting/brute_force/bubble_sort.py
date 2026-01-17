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
from utils.decorators import visualise_sort

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
        
        # Yielding the partially / fully sorted array at each step. Using copy() to avoid modifying the original list and also maintain the correct state of the array at each step
        yield unsorted_list.copy()

        # If no elements were swapped, the array is already sorted. Hence break the loop
        if not swapped:
            break

if __name__ == "__main__":
    # Calling the helper function to create a random list
    unsorted_list = create_random_list(5)
    
    # Visualising the bubble sort algorithm
    visualise_sort(execute_bubble_sort, unsorted_list)
    
"""This is the implementation of insertion sort algorithm.

Insertion sort is a simple sorting algorithm that builds the final sorted array using a key element one at a time.
This key element is compared with all the elements before it and shifts the elements to the right until the correct
position is found.
The process is repeated for all the elements in the array.
Time complexity: O(n^2)
Space complexity: O(1)

Problem Statement: Sort an array of integers in ascending order using insertion sort algorithm
N = length of the array
-500 <= ar[i] <= 500
"""

from collections.abc import Iterator
from sorting.helpers import create_random_list
from utils.decorators import visualise_sort


# Executing the insertion sort algorithm as a generator and yielding the sorted array at each step
def execute_insertion_sort(unsorted_list: list[int]) -> Iterator[list[int]]:
    """Executing the insertion sort algorithm as a generator and yielding the sorted array at each step.

    Args:
        unsorted_list (list[int]): The list of integers to be sorted.

    Returns:
        Iterator[list[int]]: The sorted array at each step.
    """
    # Executing the insertion sort algorithm
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1

        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1

        unsorted_list[j + 1] = key

        # Yielding the partially / fully sorted array at each step
        yield unsorted_list


if __name__ == "__main__":
    # Calling the helper function to create a random list
    unsorted_list = create_random_list(5)

    # Visualising the insertion sort algorithm
    visualise_sort(execute_insertion_sort, unsorted_list)

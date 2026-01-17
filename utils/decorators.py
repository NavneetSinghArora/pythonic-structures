"""
This module contains decorators for various purposes
"""

from typing import Iterator
from functools import wraps
import time
from typing import Any, Callable

# Creating a decorator to measure the time taken by a function
def timer(func) -> Callable:
    """
    Decorator to measure the time taken by a function

    Args:
        func (function): The function to be decorated
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Wrapper function to measure the time taken by a function

        Args:
            *args: The arguments to be passed to the function
            **kwargs: The keyword arguments to be passed to the function
        
        Returns:
            The result of the function
        """
        start_time = time.perf_counter()
        
        # Executing the function
        result = func(*args, **kwargs)
        
        # Calculating the time taken
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time}")
        
        # Returning the result of the function
        return result
    
    # Returning the wrapper function
    return wrapper


# Visualising the insertion sort algorithm
@timer
def visualise_sort(sorting_algorithm: Callable[[list[int]], Iterator[list[int]]], unsorted_list: list[int], sleep_time: Optional[int] = 1) -> Tuple[int, list[int]]:
    """
    Visualising the sorting algorithm
    
    Args:
        sorting_algorithm (function): The function to be decorated
        sleep_time (int, optional): The time to sleep between steps. Defaults to 1.
    
    Returns:
        Tuple[int, list[int]]: The number of steps and the sorted array
    """
    print("Initial array:", unsorted_list)
    
    steps = 0
    sorted_list = unsorted_list
    
    # Using the generator to visualise the sorting by yielding the sorted array at each step
    for _sorted_list in sorting_algorithm(unsorted_list):
        steps += 1
        sorted_list = _sorted_list

        # Adding a delay to visualise the sorting after every iteration
        time.sleep(sleep_time)
        print(f"Step {steps}: {_sorted_list}")
    
    print(f"Sorting Complteted in {steps} steps")
    print("Final Sorted List:", sorted_list)
    return steps, sorted_list
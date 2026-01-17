"""
This module contains decorators for various purposes
"""

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
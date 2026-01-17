"""
This module contains helper functions for sorting algorithms
"""

import random

def create_random_list(length: int) -> list[int]:
    """
    Creating a random list of integers

    Args:
        length (int): The length of the list

    Returns:
        list[int]: The random list of integers
    """
    return [random.randint(-500, 500) for _ in range(length)]
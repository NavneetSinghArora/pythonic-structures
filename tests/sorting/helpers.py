"""Helper functions for sorting tests."""

from sorting.helpers import create_random_list
import random


def create_random_list_and_expected_output() -> tuple[list[int], list[int]]:
    """Create a random list and expected output.

    Returns:
        tuple[list[int], list[int]]: The random list and expected output.
    """
    # Get a random list length
    list_length = random.randint(1, 10)

    # Create a random list using the random list length
    data_list = create_random_list(list_length)

    # Use the native python sorting to sort the list for the expected output
    expected_output = sorted(data_list)

    return (data_list, expected_output)

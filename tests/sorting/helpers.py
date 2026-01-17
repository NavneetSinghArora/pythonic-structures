from sorting.helpers import create_random_list
import random
from typing import Tuple

def create_random_list_and_expected_output() -> Tuple[list[int], list[int]]:
    # Get a random list length
    list_length = random.randint(1, 10)
    
    # Create a random list using the random list length
    data_list = create_random_list(list_length)

    # Use the native python sorting to sort the list for the expected output
    expected_output = sorted(data_list)

    return data_list, expected_output
    
    

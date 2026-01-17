from sorting.brute_force.bubble_sort import execute_bubble_sort
from sorting.brute_force.insertion_sort import execute_insertion_sort
from tests.sorting.helpers import create_random_list_and_expected_output
from utils.decorators import visualise_sort

def test_bubble_sort():
    # Create a random list and expected output using the helper function
    unsorted_list, sorted_list = create_random_list_and_expected_output()
    
    # Explicitly setting the sleep time to 0 to avoid delay in the test
    result_steps, result_sorted_list = visualise_sort(execute_bubble_sort, unsorted_list, 0)

    assert result_sorted_list == sorted_list


def test_insertion_sort():
    # Create a random list and expected output using the helper function
    unsorted_list, sorted_list = create_random_list_and_expected_output()
    
    # Explicitly setting the sleep time to 0 to avoid delay in the test
    result_steps, result_sorted_list = visualise_sort(execute_insertion_sort, unsorted_list, 0)

    assert result_sorted_list == sorted_list

import pytest
from sorting.brute_force.bubble_sort import execute_bubble_sort
from sorting.brute_force.insertion_sort import execute_insertion_sort
from sorting.helpers import create_random_list
from utils.decorators import visualise_sort

@pytest.mark.benchmark(group="sorting")
def test_benchmark_bubble_sort(benchmark):
    data = create_random_list(16)
    benchmark(visualise_sort, execute_bubble_sort, data, 0)

@pytest.mark.benchmark(group="sorting")
def test_benchmark_insertion_sort(benchmark):
    data = create_random_list(16)
    benchmark(visualise_sort, execute_insertion_sort, data, 0)

@pytest.mark.benchmark(group="sorting")
def test_benchmark_native_sort(benchmark):
    data = create_random_list(16)
    benchmark(sorted, data)
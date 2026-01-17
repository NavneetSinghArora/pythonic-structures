import pytest
from sorting.brute_force.bubble_sort import visualise_bubble_sort
from sorting.brute_force.insertion_sort import visualise_insertion_sort
from sorting.helpers import create_random_list

@pytest.mark.benchmark(group="sorting")
def test_benchmark_bubble_sort(benchmark):
    data = create_random_list(16)
    benchmark(visualise_bubble_sort, data, 0)

@pytest.mark.benchmark(group="sorting")
def test_benchmark_insertion_sort(benchmark):
    data = create_random_list(16)
    benchmark(visualise_insertion_sort, data, 0)

@pytest.mark.benchmark(group="sorting")
def test_benchmark_native_sort(benchmark):
    data = create_random_list(16)
    benchmark(sorted, data)
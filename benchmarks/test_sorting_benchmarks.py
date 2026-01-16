import pytest
import random
from sorting.brute_force.bubble_sort import visualise_bubble_sort

@pytest.mark.benchmark(group="sorting")
def test_benchmark_bubble_sort(benchmark):
    data = [random.randint(-500, 500) for _ in range(16)]
    benchmark(visualise_bubble_sort, data, 0)

@pytest.mark.benchmark(group="sorting")
def test_benchmark_native_sort(benchmark):
    data = [random.randint(-500, 500) for _ in range(16)]
    benchmark(sorted, data)
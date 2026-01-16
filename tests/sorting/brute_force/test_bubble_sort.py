import pytest
from sorting.brute_force.bubble_sort import visualise_bubble_sort


@pytest.mark.parametrize("balance, sorted_balance, steps", [
    (
        [91, -437, -300, -147, -96, -45, 358, 205, -476, -40],
        [-476, -437, -300, -147, -96, -45, -40, 91, 205, 358],
        9
    ),
    (
        [279, 410, 221, 293, 320, -346, -373, 451, -201, 378],
        [-373, -346, -201, 221, 279, 293, 320, 378, 410, 451],
        9
    ),
    (
        [75, 250, -347, -489, -337, 24, -82, -364, -380, 161, 152, 369, 89, 339, 469, -410],
        [-489, -410, -380, -364, -347, -337, -82, 24, 75, 89, 152, 161, 250, 339, 369, 469],
        15
    )
])
def test_bubble_sort(balance, sorted_balance, steps):
    # Explicitly setting the sleep time to 0 to avoid delay in the test
    result_steps, result_balance = visualise_bubble_sort(balance, 0)

    assert result_balance == sorted_balance
    assert result_steps == steps

import pytest
from main.sorted_frozen_set import SortedFrozenSet


@pytest.fixture
def sorted_frozen_set_sequence():
    return SortedFrozenSet([1, 4, 9, 13, 15])


def test_index_zero(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[0] == 1


def test_index_four(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[4] == 15


def test_index_one_beyond_the_end(sorted_frozen_set_sequence):
    with pytest.raises(IndexError):
        _ = sorted_frozen_set_sequence[5]


def test_index_minus_one(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[-1] == 15


def test_index_minus_five(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[-5] == 1


def test_index_one_before_beginning(sorted_frozen_set_sequence):
    with pytest.raises(IndexError):
        _ = sorted_frozen_set_sequence[-6]


def test_slice_from_start(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[:3] == SortedFrozenSet([1, 4, 9])


def test_slice_to_end(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[3:] == SortedFrozenSet([13, 15])


def test_slice_empty(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[10:] == SortedFrozenSet()


def test_slice_arbitrary(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[2:4] == SortedFrozenSet([9, 13])


def test_slice_step(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[0:5:2] == SortedFrozenSet([1, 9, 15])


def test_slice_full(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence[:] == SortedFrozenSet([1, 4, 9, 13, 15])


def test_reversed():
    s = SortedFrozenSet([1, 3, 5, 7])

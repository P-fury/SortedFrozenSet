from collections.abc import Sequence

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
    r = reversed(s)
    assert next(r) == 7
    assert next(r) == 5
    assert next(r) == 3
    assert next(r) == 1

    with pytest.raises(StopIteration):
        next(r)


def test_index_positive(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence.index(1) == 0


def test_index_negative(sorted_frozen_set_sequence):
    with pytest.raises(ValueError):
        sorted_frozen_set_sequence.index(5)


def test_count_zero(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence.count(5) == 0


def test_count_one(sorted_frozen_set_sequence):
    assert sorted_frozen_set_sequence.count(4) == 1


def test_add_disjoint():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([4, 5, 6])

    assert s + t == SortedFrozenSet([1, 2, 3, 4, 5, 6])


def test_add_equal():
    s = SortedFrozenSet([1, 2, 3])
    assert s + s == s


def test_add_intersecting():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([2, 3, 4])

    assert s + t == SortedFrozenSet([1, 2, 3, 4])


def test_add_type_error_left():
    s = SortedFrozenSet([1, 2, 3])
    t = (3, 4, 5)
    with pytest.raises(TypeError):
        _ = s + t


def test_add_type_error_right():
    t = (3, 4, 5)
    s = SortedFrozenSet([1, 2, 3])
    with pytest.raises(TypeError):
        _ = s + t


def test_repetition_zero_left():
    s = SortedFrozenSet([1, 2, 3])
    assert s * 0 == SortedFrozenSet()


def test_repetition_negative_left():
    s = SortedFrozenSet([1, 2, 3])
    assert s * -1 == SortedFrozenSet()


def test_repetition_non_zero_left():
    s = SortedFrozenSet([1, 2, 3])
    assert s * 100 == s


def test_repetition_zero_right():
    s = SortedFrozenSet([1, 2, 3])
    assert 0 * s == SortedFrozenSet()


def test_repetition_negative_right():
    s = SortedFrozenSet([1, 2, 3])
    assert -1 * s == SortedFrozenSet()


def test_repetition_non_zero_right():
    s = SortedFrozenSet([1, 2, 3])
    assert 100 * s == s

def test_sequence_protocol():
    assert issubclass(SortedFrozenSet, Sequence)

# extended sequence
# immutable/mutable -> __add__/__radd__, __mul__/__rmul__
# only mutable -> __iadd__, __imul__, append, extend, insert, pop, reverse, remove, sort

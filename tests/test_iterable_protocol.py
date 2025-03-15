from collections.abc import Iterable

import pytest

from main.sorted_frozen_set import SortedFrozenSet


@pytest.fixture
def sorted_frozen_set_duplicates():
    return SortedFrozenSet([7, 2, 1, 1, 9])


def test_iter(sorted_frozen_set_duplicates):
    iterator = iter(sorted_frozen_set_duplicates)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 7
    assert next(iterator) == 9

    with pytest.raises(StopIteration):
        next(iterator)


def test_for_loop(sorted_frozen_set_duplicates):
    expected = [1, 2, 7, 9]

    for idx, item in enumerate(sorted_frozen_set_duplicates):
        assert item == expected[idx]


def test_iterable_protocol():
    assert issubclass(SortedFrozenSet, Iterable)
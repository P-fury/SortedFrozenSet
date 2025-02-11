from collections.abc import Iterable

from main.sorted_frozen_set import SortedFrozenSet


def test_construct_empty():
    SortedFrozenSet([])


def test_construct_from_non_empty_list():
    SortedFrozenSet([7, 8, 3, 1])


def test_construct_from_an_iterable():
    items = [7, 8, 3, 1]
    iterator = iter(items)
    SortedFrozenSet(iterator)


def test_construct_no_args():
    s = SortedFrozenSet()
    assert isinstance(s._items, Iterable)

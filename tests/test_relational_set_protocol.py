from main.sorted_frozen_set import SortedFrozenSet


def test_lt():
    s = SortedFrozenSet([1, 2])
    t = SortedFrozenSet([1, 2, 3])
    assert s < t


def test_le_lt():
    s = SortedFrozenSet([1, 2])
    t = SortedFrozenSet([1, 2, 3])
    assert s <= t


def test_le_eq():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([1, 2, 3])
    assert s <= t


def test_gt():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([1, 2])
    assert s > t


def test_ge_gt():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([1, 2])
    assert s >= t


def test_ge_eq():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([1, 2, 3])
    assert s >= t

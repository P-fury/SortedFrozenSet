from main.sorted_frozen_set import SortedFrozenSet


def test_positive_unequal():
    assert SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([1, 2, 3])


def test_negative_unequal():
    assert not (SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([6, 5, 4]))


def test_type_mismatch():
    assert SortedFrozenSet([4, 5, 6]) != [4, 5, 6]


def test_identical():
    s = SortedFrozenSet([4, 5, 6])
    assert not (s != s)

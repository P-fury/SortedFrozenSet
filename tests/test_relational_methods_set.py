from main.sorted_frozen_set import SortedFrozenSet


def test_issubset_proper():
    s = SortedFrozenSet([1, 2])
    t = SortedFrozenSet([1, 2, 3])
    assert s.issubset(t)


def test_issubset():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([1, 2, 3])
    assert s.issubset(t)


def test_issuperset_proper():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([1, 2])
    assert s.issuperset(t)


def test_issuperset():
    t = SortedFrozenSet([1, 2, 3])
    s = SortedFrozenSet([1, 2, 3])
    assert s.issuperset(t)


def test_isdisjoint():
    t = SortedFrozenSet([1, 2, 3])
    s = SortedFrozenSet([4, 5, 6])
    assert s.isdisjoint(t)

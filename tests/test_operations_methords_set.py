from main.sorted_frozen_set import SortedFrozenSet


def test_intersection():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s.intersection(t) == SortedFrozenSet({2, 3})


def test_union():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s.union(t) == SortedFrozenSet({1, 2, 3, 4})


def test_symmetric_difference():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})
    assert s.symmetric_difference(t) == SortedFrozenSet({1, 4})


def test_difference():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})
    assert s.difference(t) == SortedFrozenSet({1})

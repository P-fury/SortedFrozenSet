from collections.abc import Container

import pytest

from main.sorted_frozen_set import SortedFrozenSet


@pytest.fixture
def sorted_frozen_set():
    return SortedFrozenSet([6, 7, 3, 9])


def test_positive_contained(sorted_frozen_set):
    assert 3 in sorted_frozen_set


def test_negative_contained(sorted_frozen_set):
    assert 15 not in sorted_frozen_set


def test_positive_not_contained(sorted_frozen_set):
    assert 15 not in sorted_frozen_set


def test_negative_not_contained(sorted_frozen_set):
    assert not (3 not in sorted_frozen_set)

def test_container_protocol():
    assert issubclass(SortedFrozenSet, Container)
from bisect import bisect_left
from collections.abc import Iterable, Hashable, Iterator, Sequence
from itertools import chain
from typing import Any

from main.sorted_frozen_dtypes import SupportsRichComparisonT, SupportsRichComparison


class SortedFrozenSet(Sequence):
    def __init__(self, items: Iterable[SupportsRichComparisonT] | None = None) -> None:
        self._items: tuple[SupportsRichComparisonT, ...] = tuple(
            sorted(
                set(items) if items is not None
                else set()
            ))

    def __contains__(self, item) -> bool:
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[SupportsRichComparison]:
        return iter(self._items)

    def __getitem__(self, index: int | slice) -> Any:
        items: SupportsRichComparison | tuple[SupportsRichComparison] = self._items[index]

        if isinstance(index, slice) and isinstance(items, tuple):
            return SortedFrozenSet(items)
        return items

    def __repr__(self) -> str:
        return (f"{type(self).__name__}"
                f"({f'[{", ".join(map(repr, self._items))}]' if self._items else ''})")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items

    def __hash__(self) -> int:
        return hash(tuple(self._items))

    def __add__(self, other: Any) -> 'SortedFrozenSet':
        if not isinstance(other, type(self)):
            return NotImplemented
        return SortedFrozenSet(chain(self._items, other._items))

    def __mul__(self, other: Any) -> 'SortedFrozenSet':
        return self if other > 0 else SortedFrozenSet()

    def __rmul__(self, other: Any) -> 'SortedFrozenSet':
        return self * other

    def count(self, item):
        return int(item in self)

    def index(self, item: Any) -> int:
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError(f'{item!r} not found')

    # def __next__(self) -> Hashable:
    #     return self._items.pop()

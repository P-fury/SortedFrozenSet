from collections.abc import Iterable, Hashable



class SortedFrozenSet:
    def __init__(self, items: Iterable[Hashable] | None = None) -> None:
        self._items: Iterable[Hashable] = items or []

    def __contains__(self, item: Hashable) -> bool:
        return item in self._items

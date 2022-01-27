from abc import abstractmethod
from collections.abc import MutableSequence
from typing import overload, _T, Iterable, Any, Optional


class LinkedList(MutableSequence):
    def __init__(self, value: ):


    def insert(self, index: int, value: _T) -> None:
        pass

    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> _T: ...

    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> MutableSequence[_T]: ...

    def __getitem__(self, i: int) -> _T:
        pass

    @overload
    @abstractmethod
    def __setitem__(self, i: int, o: _T) -> None: ...

    @overload
    @abstractmethod
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...

    def __setitem__(self, i: int, o: _T) -> None:
        pass

    @overload
    @abstractmethod
    def __delitem__(self, i: int) -> None: ...

    @overload
    @abstractmethod
    def __delitem__(self, i: slice) -> None: ...

    def __delitem__(self, i: int) -> None:
        pass

    def __len__(self) -> int:
        pass


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ...

from abc import abstractmethod
from collections.abc import MutableSequence
from typing import overload, _T, Iterable, Any, Optional

from node import #fixme

class LinkedList(MutableSequence):
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.len = 0

    def is_valid(self, node: Optional["Node"] = None):

        if not isinstance(node, (Node, type(None))):
            raise TypeError("Передана не нода")

    def step_by_step(self, index) -> "Node":
        if index < 0:
            raise ValueError("Передано отрицательно число")

        if index > self.len - 1:
            raise ValueError("Передан индекс, превышающий значение длины списка")

        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")

        return self[index]

    def test_step_by_step

        #ожидаю увидеть возвращенный узел

    def __len__(self) -> int:
        return self.len


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

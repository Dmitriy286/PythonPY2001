from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        prev__ = None if self.prev is None else f"{self.__class__.__name__}(\"{self.value}\")"
        next__ = None if self.next is None else f"{self.__class__.__name__}(\"{self.value}\")"
        return f"{self.__class__.__name__}(\"{self.value}\", {next__}, {prev__})"



    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node, DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self._prev = prev


if __name__ == "__main__":
    # DLNode_1 = DoubleLinkedNode("Value_1")
    DLNode_0 = DoubleLinkedNode("Value_0")
    DLNode_2 = DoubleLinkedNode("Value_2")

    LinkedNode = DoubleLinkedNode("Value_1", DLNode_0, DLNode_2)
    print(repr(DLNode_0))
    print(repr(DLNode_2))
    print(repr(LinkedNode))

# TODO реализовать класс DoubleLinkedNode

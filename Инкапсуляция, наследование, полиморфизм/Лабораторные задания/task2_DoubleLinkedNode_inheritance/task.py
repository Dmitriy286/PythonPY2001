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
    def __init__(self, value, next_: Optional["DoubleLinkedNode"] = None, prev: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev #todo getter and setter

    def __repr__(self) -> str:
        next__ = None if self.next is None else self.next
        prev__ = None if self.prev is None else self.prev
        return f"{self.__class__.__name__}({self.value}, {next__}, {prev__})"


    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        self.is_valid(prev)
        self._prev = prev

# TODO реализовать класс DoubleLinkedNode

if __name__ == "__main__":
    dln_1 = DoubleLinkedNode("1 value")
    dln_0 = DoubleLinkedNode("0 value")
    dln_2 = DoubleLinkedNode("2 value")
    print(str(dln_1))
    print(repr(dln_1))
    dln_ll = DoubleLinkedNode("4 value", dln_0, dln_2)
    print(str(dln_ll))
    print(dln_ll)
    print(type(dln_ll))
from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

    @classmethod
    def is_valid(cls, node: Any):
        """
        Метод проверки валидности переданной ноды
        :return:
        """
        if not isinstance(node, (type(None), cls)):
            raise TypeError("Не нода передана")

    def __str__(self):
        """
        Метод возвращает человекочитаемое представление
        :return:
        """
        return f"{self.__class__.__name__}({self.value})"

    def __repr__(self):
        next__ = None if self.next is None else self.next
        return f"{self.__class__.__name__}({repr(self.value)}, {repr(next__)})"


class DoubleLinkedNode(Node):

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self):
        next__ = None if self.next is None else self.next
        prev__ = None if self.prev is None else self.prev

        return f"{self.__class__.__name__} ({repr(self.value)}, {repr(prev__)}, {repr(next__)})"


if __name__ == "__main__":
    ...

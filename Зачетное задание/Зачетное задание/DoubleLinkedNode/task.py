from typing import Any, Optional

class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

        self.is_valid()

    @property
    def next(self):
        return self._next_

    @next.setter
    def next(self, next_):
        if not isinstance(next_, Node):
            raise TypeError("Передана не нода")
        self._next_ = next_

    def is_valid(self):
        """
        Метод
        :return:
        """
        if not isinstance(self, Node):
            raise TypeError("Не нода передана")

    def __str__(self):
        """
        Метод возвращает человекочитаемое представление
        :return:
        """
        return f"{self.__class__.__name__} ({self.value})"

    def __repr__(self):
        if self.next == None:
            next__ = None
        else:
            next__ = self.next
        return f"{self.__class__.__name__} ({repr(self.value)}, {repr(next__)})"

class DoubleLinkedNode(Node):
    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        if not isinstance(prev, DoubleLinkedNode):
            raise TypeError("Передана не двусвязная нода")
        self._prev = prev

    # def is_valid(self):
    #     """
    #     Метод
    #     :return:
    #     """
    #     if not isinstance(self, Node):
    #         raise TypeError("Не нода передана")
    #
    # def __repr__(self):
    #     if self.next == None:
    #         next__ = None
    #     else:
    #         next__ = self.next
    #     return f"{self.__class__.__name__} ({repr(self.value)}, {repr(next__)})"

if __name__ == "__main__":
    ...

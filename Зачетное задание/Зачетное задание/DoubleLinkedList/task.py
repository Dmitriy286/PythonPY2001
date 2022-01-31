from collections.abc import MutableSequence
from typing import Optional, Any, Iterable, Iterator

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable):
        # self.data = data
        self.len = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        if self is None:
            for value in data:
                self.append(value)
                self.len += 1

    def __iter__(self) -> Iterator:
        """
        Метод, превращающий связный список в итератор
        :return:
        """
        return self

    @staticmethod
    def linked_nodes(left_node: "Node", right_node: "Node"):
        left_node.next = right_node

    def index_valid(self, index):
        if not isinstance(index, int):
            raise TypeError("Передано не число")

        if index < 0 or index >= self.len:
            raise ValueError("Переданное число выходит за границы допустимого диапазона")

    def step_by_step_for_node(self, index):
        """
        Метод возвращает ноду  по индексу
        :param index: индекс, по которому необходимо вернуть ноду
        :return:
        """
        self.index_valid(index)
        return self[index]

    def __getitem__(self, index: int) -> Any:
        """
        Метод, возвращающий значение ноды по индексу
        :param index: индекс, целое число
        :return: значение ноды по индексу
        """
        self.index_valid(index)
        node = self.step_by_step_for_node(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Метод устанавливает в ноду по индексу переданное значение
        :param index: индекс
        :param value: значение
        :return: None
        """
        self.index_valid(index)
        self.step_by_step_for_node(index).value = value

    def __delitem__(self, index: int) -> None:
        """
        Метод удаляет ноду по индексу
        :param index:
        :return:
        """
        self.index_valid(index)
        delited_node = self.step_by_step_for_node(index)


    def __len__(self) -> int:
        pass

    def insert(self, index: int, value: _T) -> None:
        pass


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ...

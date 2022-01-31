from collections.abc import MutableSequence
from typing import Optional, Any, Iterable, Iterator

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        # self.data = data
        self._len = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        for value in data:
            self.append(value)

    def __len__(self) -> int:
        """
        Метод устанавливает длину связанного списка
        :return: целое число
        """
        self._len = len(self)
        return self._len

    def __iter__(self) -> Iterator:
        """
        Метод, превращающий связный список в итератор
        :return:
        """
        return self

    @staticmethod
    def linked_nodes(left_node: "Node", right_node: Optional["Node"] = None):
        left_node.next = right_node

    def index_valid(self, index):
        if not isinstance(index, int):
            raise TypeError("Передано не число")

        if index < 0 or index >= self._len:
            raise ValueError("Переданное число выходит за границы допустимого диапазона")

        return index

    def step_by_step_for_node(self, index):
        """
        Метод возвращает ноду по индексу
        :param index: индекс, по которому необходимо вернуть ноду
        :return:
        """
        self.index_valid(index)
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

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
        previous_node = self.step_by_step_for_node(index - 1)
        next_node = self.step_by_step_for_node(index + 1)
        self.linked_nodes(previous_node, next_node)
        delited_node.next = None
        self._len -= 1

    def append(self, value: Any):
        if self._len == 0:
            append_node = Node(value)
            self.head = self.tail = append_node

        else:
            append_node = Node(value)
            current_node = self.step_by_step_for_node(self._len - 1)
            self.linked_nodes(current_node, append_node)
            self.tail = append_node

        self._len += 1

    def insert(self, index: int, value: Any) -> None:
        self.index_valid(index)
        append_node = Node(value)
        if index == 0:
            self.linked_nodes(append_node, self.head)
            self.head = append_node

        elif index >= self._len:
            self.append(value)

        else:
            current_node = self.step_by_step_for_node(index - 1)
            next_node = self.step_by_step_for_node(index)
            append_node = Node(value)
            self.linked_nodes(append_node, next_node)
            self.linked_nodes(current_node, append_node)

        self._len += 1

    def list_of_nodes(self) -> list:
        """
        Метод возвращает список нод
        :return:
        """
        return [node for node in self]

    def __str__(self) -> str:
        return f"{self.list_of_nodes()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.list_of_nodes()})"

class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ll_1 = LinkedList([1, 2, 3])
    print(str(ll_1))
    print(repr(ll_1))

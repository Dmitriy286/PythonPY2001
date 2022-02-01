from collections.abc import MutableSequence
from typing import Optional, Any, Iterable, Iterator

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    ClASS_NAME = Node
    def __init__(self, data: Iterable = None):

        self._len = 0
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def __len__(self) -> int:
        """
        Метод устанавливает длину связанного списка
        :return: целое число
        """
        return self._len


    # def __iter__(self) -> Iterator:
    #     """
    #     Метод, превращающий связный список в итератор
    #     :return:
    #     """
    #     len(self)
    #     #нужно функцию генератор
    #     current_node = self._head
    #     for _ in range(len(self)):
    #         yield current_node.value
    #         current_node = current_node.next
    #fixme почему не нужен iter?

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node

    def index_valid(self, index):
        if not isinstance(index, int):
            raise TypeError("Передано не число")

        if index < 0 or index >= self._len:
            raise ValueError("Переданное число выходит за границы допустимого диапазона")

    def step_by_step_for_node(self, index):
        """
        Метод возвращает ноду по индексу
        :param index: индекс, по которому необходимо вернуть ноду
        :return:
        """
        if not isinstance(index, int):
            raise TypeError("Передано не число")

        # if index < 0 or index >= self._len:
        if not 0 <= index < self._len:
            raise IndexError("Переданное число выходит за границы допустимого диапазона")

        # self.index_valid(index)
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """
        Метод, возвращающий значение ноды по индексу
        :param index: индекс, целое число
        :return: значение ноды по индексу
        """
        # self.index_valid(index)
        node = self.step_by_step_for_node(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Метод устанавливает в ноду по индексу переданное значение
        :param index: индекс
        :param value: значение
        :return: None
        """
        # self.index_valid(index)
        self.step_by_step_for_node(index).value = value

    def __delitem__(self, index: int) -> None:
        """
        Метод удаляет ноду по индексу
        :param index:
        :return:
        """
        # self.index_valid(index)
        deleted_node = self.step_by_step_for_node(index)

        if self._len == 1:
            self._head = None
            self._tail = None
        elif index == 0:
            next_node = self.step_by_step_for_node(index + 1)
            self._head = next_node
            deleted_node.next = None
        elif index >= self._len - 1:
            previous_node = self.step_by_step_for_node(index - 1)
            self._tail = previous_node
            previous_node.next = None
        else:
            next_node = self.step_by_step_for_node(index + 1)
            previous_node = self.step_by_step_for_node(index - 1)
            self.linked_nodes(previous_node, next_node)
            deleted_node.next = None

        self._len -= 1

    def append(self, value: Any):
        append_node = self.ClASS_NAME(value)

        if self._len == 0:
        # if self._head is None:
            self._head = self._tail = append_node

        else:
            current_node = self.step_by_step_for_node(self._len - 1)
            self.linked_nodes(current_node, append_node)
            self.tail = append_node

            # self.linked_nodes(self._tail, append_node)
            # self._tail = append_node

        self._len += 1

    def insert(self, index: int, value: Any) -> None:
        # self.index_valid(index)
        append_node = self.ClASS_NAME(value)
        if index == 0:
            self.linked_nodes(append_node, self._head)
            self._head = append_node
            self._len += 1
        elif index >= self._len:
            self.append(value)
        else:
            current_node = self.step_by_step_for_node(index - 1)
            next_node = self.step_by_step_for_node(index)
            append_node = self.ClASS_NAME(value)
            self.linked_nodes(append_node, next_node)
            self.linked_nodes(current_node, append_node)

            self._len += 1

    def list_of_nodes(self) -> list:
        """
        Метод возвращает список нод
        :return:
        """
        return [node_value for node_value in self]

    def __str__(self) -> str:
        return f"{self.list_of_nodes()}"

    def __repr__(self) -> str:
    #     # node = Node(value, next_)
    #     # return f"{self.__class__.__name__}(node for node )"
    #
    #     for value in self:
    #         for node in self.list_of_nodes():
    #             yield f"{self.__class__.__name__}({value}, {node})"

        return f"{self.__class__.__name__}({self.list_of_nodes()})"

class DoubleLinkedList(LinkedList):
    ClASS_NAME = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

if __name__ == "__main__":
    ll_1 = LinkedList([1, 2, 3, 4, 5])
    print(str(ll_1))
    print(repr(ll_1))
    print(repr(ll_1.list_of_nodes()))
    print(ll_1)
    print(repr(ll_1.step_by_step_for_node(2)))

    ll_2 = DoubleLinkedList([1, 2, 3, 4, 5])
    print(str(ll_2))
    print(repr(ll_2))
    print(repr(ll_2.list_of_nodes()))
    print(ll_2)
    print(ll_2.step_by_step_for_node(1))
    print(ll_2.step_by_step_for_node(1).next)
    print(ll_2.step_by_step_for_node(1).prev)
    print(repr(ll_2.step_by_step_for_node(2)))

    ll_3 = DoubleLinkedList([1])
    print(str(ll_3))
    print(repr(ll_3))



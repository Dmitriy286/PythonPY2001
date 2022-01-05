from typing import Iterable, Optional, Any

from node import Node

class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        for value in data:
            self.append(value)# TODO инициализировать связный список

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        if index is None:
            index = self.len - 1

        node = self.step_by_step_on_nodes(index)
        return node.value

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __len__(self):
        return self.len

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        # TODO реализовать алгоритм добавления узла в конец последовательности
        append_node = Node(value) # right_node
        if self.head is None:
            self.head = append_node
        else:
            last_node = self.step_by_step_on_nodes(self.len - 1) # left_node
            self.linked_nodes(last_node, append_node)
        self.len += 1

    def extend(self, iterable):
        for iter_value in iterable:

            last_node = self.step_by_step_on_nodes(self.len - 1)
            new_node = Node(iter_value)
            self.linked_nodes(last_node, new_node)

            self.len += 1

    def __delitem__(self, index: int):

        if not isinstance(index, int):
            raise TypeError("Введено не число")  # TODO проверка индекса

        if not 0 <= index < self.len:
            raise IndexError("Переданный индекс выходит за рамки длины списка")


        if index == 0:
            if self.len > 1:
                self.head = self.step_by_step_on_nodes(index + 1)
                self.step_by_step_on_nodes(index).next = None
                self.len -= 1
            else:
                    self.head = None
                    self.len = 0

        elif index == self.len - 1:
            previous_node = self.step_by_step_on_nodes(index - 1)
            previous_node.next = None
            self.len -= 1
        else:
            delited_node = self.step_by_step_on_nodes(index)
            pre_delited_node = self.step_by_step_on_nodes(index - 1)
            post_delited_node = self.step_by_step_on_nodes(index + 1)
            # pre_delited_node.next = post_delited_node
            # delited_node.next = None
            self.linked_nodes(pre_delited_node, post_delited_node)
            delited_node.next = None

            self.len -= 1

    # def None_proof(self):
    #     if self is None:
    #         raise ValueError("Нечего удалять")


    def pop(self, index: Optional[int] = None):
        # self.None_proof()
        if index is None:
            index = self.len - 1

        else:
            if index >= self.len:
                raise IndexError("Индекс за пределами диапазона")

        node = self.step_by_step_on_nodes(index)

        self.__delitem__(index)

        return node.value


if __name__ == "__main__":
    list_ = [4, 1, 4, "wow"]

    ll = LinkedList(list_)
    print(ll)

    print(ll.pop())

    print(ll.pop(1))


    ll.pop(1)
    print(ll)

    ll.pop(0)
    print(ll)

    # ll.pop(0)
    # print(ll)


#fixme как реализовать функция проверки, что self is None?
from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode as Dll


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self._head: Optional[Node] = None
        self.tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self._head is None:
            self._head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self._head
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
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


class DoubleLinkedList(LinkedList):

    # не вижу смысла в переопределении конструктора - он принимает тот же аргумент (data)
    # все работает после переопределения только одного метода linked_nodes.
    # Есть ли смысл в переопределении еще чего-либо?

    # Как инкапсулировать методы?

    @staticmethod
    def linked_nodes(left_node: Dll, right_node: Optional[Dll] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел

        """
        left_node.next = right_node
        right_node.prev = left_node  #добавил ссылку правой ноды на предыдущую

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Dll(value)

        if self._head is None:
            self._head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    @property
    def head(self):
        return self._head



    # возможно, нужно инкапсулировать head и tail, потому что получается их изменять в ифмэйне. Как это сделать?
    # моя попытка (не работает):

    # @property
    # def head(self):
    #     return self._head
    #
    # @head.setter
    # def head(self, node):
    #     if not isinstance(node, (type(None), Node)):
    #         raise TypeError("Руки прочь")
    #     self._head = None




if __name__ == "__main__":
    dll_1 = DoubleLinkedList([1, 2, 3, 4])
    print(str(dll_1))
    print(repr(dll_1))
    print(dll_1[1])
    print(repr(dll_1.head))
    print(repr(dll_1.tail))
    # dll_1.head = 1
    print(repr(dll_1.head))
    print(repr(dll_1.tail))
    print(str(dll_1))
    print(repr(dll_1))

    print(type(dll_1.head))

# TODO Реализовать класс DoubleLinkedList

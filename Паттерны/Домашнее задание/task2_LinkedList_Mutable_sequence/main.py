# TODO Реализовать LinkedList как MutableSequence
from collections.abc import MutableSequence
from typing import Any, Optional
from typing import overload

from


class LinkedList(MutableSequence):
    def __init__(self):
        super().__init__()
        # self.len = self.__len__()

    def __len__(self):
        return self.len

    def __getitem__(self, i: int) -> Any:
        return self[i].value

    def __setitem__(self, i: int, o: Any) -> None:
        self[i].value = o

    def __delitem__(self, i: int) -> None:

        if self.len - 1 < i < 0:
            raise ValueError()

        if i == 0:
            self[i].next = self.head
            self[i].next = None

        elif i == self.len - 1:
            self[i-1].next = None
            self[i - 1] = self.tail

        else:
            self[i-1].next = self[i+1]
            self[i].next = None

        self.len -= 1

    def insert(self, index: int, value: Any) -> None:
        if self.len - 1 < i < 0:
            raise ValueError()

        if i == 0:
            current_node = self(value)
            self.head = current_node
            self.head.next = self[i]

        elif i > self.len - 1:
            current_node = self(value)
            self[self.len - 1].next = current_node
            self.tail = current_node

        else:
            current_node = self(value)
            current_node.next = self[i]
            self[i - 1].next = current_node

        self.len += 1

#     def step_by_step(self) -> "Node":
#         ...
#
#
# class DoubleLL(LinkedList):
#     ...
#     @overload
#     def step_by_step(self) -> "dLLNode":
#         ...
#

if __name__ == "__main__":
    linked_list = LinkedList([1, 2, 3])
    print(linked_list)
    print(type(linked_list))
    print(linked_list.__dict__)

    # list_ = [1, 2, 3]
    # linked_list = LinkedList(list_)
    # print(linked_list)
    #
    # print(linked_list[1])

#fixme прошу проверить дз
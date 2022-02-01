from typing import Any, Optional

from node import DoubleLinkedNode
from task import DoubleLinkedList


class DoubleLinkedListR(DoubleLinkedList):
    def index_search(self, value: Any) -> int:
        index = 0
        for node_value in self:
            if value == node_value:
                print(index)
                print(self._len)
                return index
            else:
                index += 1

    def remove(self, value: Any):

        if value in self:
            self.__delitem__(self.index_search(value))
        else:
            raise ValueError("Значения нет в линкед листе")


if __name__ == "__main__":
    ll = DoubleLinkedListR([1, 2, "3", 4, 5, 6, "6", 7])
    print(repr(ll))
    ll.remove(7)
    print(repr(ll))
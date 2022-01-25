# TODO Реализовать LinkedList как MutableSequence
from collections.abc import MutableSequence

class LinkedList(MutableSequence):
    ...


if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list.__dict__)

    # list_ = [1, 2, 3]
    # linked_list = LinkedList(list_)
    # print(linked_list)
    #
    # print(linked_list[1])
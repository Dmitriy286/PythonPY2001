import unittest

from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList
from Remove import DoubleLinkedListR

class TestRemove(unittest.TestCase):
    def test_index_search(self):
        ll = DoubleLinkedListR([1, 2, 3, 4, 5])

        self.assertEqual(1, ll.index_search(2))

    def test_index_search_2(self):
        ll = DoubleLinkedListR([1, 2, 3, 4, 5])

        self.assertEqual(2, ll.__getitem__(ll.index_search(2)))

    def test_len(self):
        ll = DoubleLinkedListR([1, 2, 3, 4, 5])
        len_ = ll._len
        ll.remove(3)
        self.assertEqual(len_ - 1, ll._len)

    def test_delete_from_empty_list(self):
        ll = DoubleLinkedListR([])

        with self.assertRaises(ValueError, msg="При удалении из пустого списка вызывается ошибка Value Error"):
            ll.remove(3)

    def test_delete_from_one_node_list(self):
        one_node_ll = DoubleLinkedListR([1])
        one_node_ll.remove(1)
        self.assertEqual("DoubleLinkedListR([])", repr(one_node_ll))

    def test_remove(self):
        ll = DoubleLinkedListR([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError, msg="При передаче отсутствующего в списке значения должна вызываться ошибка ValueError"):
            ll.remove(6)


if __name__ == '__main__':
    unittest.main()

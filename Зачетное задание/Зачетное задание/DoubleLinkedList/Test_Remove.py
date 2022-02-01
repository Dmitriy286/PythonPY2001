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

    def test_remove(self):
        ll = DoubleLinkedListR([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError, msg="При передаче отсутствующего в списке значения должна вызываться ошибка ValueError"):
            ll.remove(6)


if __name__ == '__main__':
    unittest.main()

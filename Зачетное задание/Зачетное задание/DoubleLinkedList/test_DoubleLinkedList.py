import unittest

from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList


class TestLinkedList(unittest.TestCase):
    def test_step_by_step_for_node(self):
        ll_1 = LinkedList([1, 2, 3, 4])
        self.assertEqual("Node(3)", ll_1.step_by_step_for_node(2))

    def test_repr_linked_list(self):
        ll_1 = LinkedList([1, 2, 3, 4])
        self.assertEqual("LinkedList([1, 2, 3, 4])", repr(ll_1))

    def test_insert_out_of_range(self):
        ll = LinkedList([1, 2, 3])
        ll.insert(len(ll) + 100, 100)

        self.assertEqual(4, len(ll))
        self.assertEqual("LinkedList([1, 2, 3, 100])", repr(ll))

        self.assertEqual(100, ll.tail.value)


class TestDoubleLinkedList(unittest.TestCase):
    ...

if __name__ == '__main__':
    unittest.main()

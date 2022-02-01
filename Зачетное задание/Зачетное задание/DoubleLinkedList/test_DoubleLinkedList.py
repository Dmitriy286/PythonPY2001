import unittest

from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList


class TestLinkedNode(unittest.TestCase):
    def test_step_by_step_for_node(self):
        node = Node(5)
        self.assertEqual(True, False)

    def test_repr_linked_list(self):
        ll_1 = LinkedList([1, 2, 3, 4])
        self.assertEqual("LinkedList([1, 2, 3, 4])", repr(ll_1))


class TestDoubleLinkedNode(unittest.TestCase):
    ...

if __name__ == '__main__':
    unittest.main()

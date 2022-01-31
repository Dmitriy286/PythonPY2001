import unittest

from node import Node, DoubleLinkedNode


class TestNode(unittest.TestCase):
    def test_str(self):
        node = Node(1)
        self.assertEqual("Node(1)", str(node))

    def test_repr_node(self):
        node = Node(2)
        self.assertEqual("Node(2, None)", repr(node))

    def test_is_valid(self):
        node = Node(3)

        with self.assertRaises(TypeError):
            node.is_valid(123)

    def test_next_getter(self):
        node_1 = Node(4)
        node_2 = Node(5, node_1)

        self.assertIsInstance(node_2.next, node_1.__class__)


class TestDLNode(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()

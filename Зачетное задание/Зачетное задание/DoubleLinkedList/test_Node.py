import unittest

from node import Node, DoubleLinkedNode as Dll


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
    def test_repr(self):
        dl_node_1 = Dll(1)
        dl_node_2 = Dll(2)
        dl_node_3 = Dll(3, dl_node_1, dl_node_2)

        self.assertEqual("DoubleLinkedNode (3, DoubleLinkedNode (2, None, None), DoubleLinkedNode (1, None, None))", repr(dl_node_3))

if __name__ == '__main__':
    unittest.main()

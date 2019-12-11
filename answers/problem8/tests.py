import unittest
from answer import tree_search, Node

class Testing(unittest.TestCase):
    def test_tree_search(self):
        node_a = Node(0)
        node_b = Node(1)
        node_c = Node(0)
        node_d = Node(1)
        node_e = Node(0)
        node_f = Node(1)
        node_g = Node(1)
        node_a.left = node_b
        node_a.right = node_c
        node_c.left = node_d
        node_c.right = node_e
        node_d.left = node_f
        node_d.right = node_g

        expected = 5
        actual = tree_search(node_a)

        self.assertEqual(expected, actual)
    
    def test_tree_search1(self):
        node_a = Node(0)
        node_b = Node(1)
        node_c = Node(0)
        node_d = Node(1)
        node_e = Node(0)
        node_f = Node(1)
        node_g = Node(1)
        node_a.left = node_b
        node_a.right = node_c
        node_c.left = node_d
        node_c.right = node_e
        node_d.left = node_f
        node_d.right = node_g

        expected = 4
        actual = tree_search(node_c)

        self.assertEqual(expected, actual)
    
    def test_tree_search2(self):
        node_a = Node(0)
        node_b = Node(1)
        node_c = Node(0)
        node_d = Node(1)
        node_e = Node(0)
        node_f = Node(1)
        node_g = Node(1)
        node_a.left = node_b
        node_a.right = node_c
        node_c.left = node_d
        node_c.right = node_e
        node_d.left = node_f
        node_d.right = node_g

        expected = 1
        actual = tree_search(node_g)

        self.assertEqual(expected, actual)
    
    def test_tree_search3(self):
        node_a = Node(0)
        node_b = Node(1)
        node_c = Node(0)
        node_d = Node(1)
        node_e = Node(0)
        node_f = Node(1)
        node_g = Node(1)
        node_a.left = node_b
        node_a.right = node_c
        node_c.left = node_d
        node_c.right = node_e
        node_d.left = node_f
        node_d.right = node_g

        expected = 3
        actual = tree_search(node_d)

        self.assertEqual(expected, actual)

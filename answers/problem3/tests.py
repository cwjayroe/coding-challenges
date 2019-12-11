import unittest
from answer import serialize, Node, deserialize

class Testing(unittest.TestCase):
    def test_serialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        expected_result = ['root', 'left', 'left.left', 'right']

        actual_result = serialize(node)

        self.assertEquals(expected_result, actual_result)
    
    def test_deserialize(self):
        node_array = ['root', 'left', 'left.left', 'right']
        test_node = Node('root', Node('left', Node('left.left')), Node('right'))
        actual_node = deserialize(node_array)

        actual_result = test_node.left.left.val
        expected_result = actual_node.left.left.val

        self.assertEquals(actual_result, expected_result)


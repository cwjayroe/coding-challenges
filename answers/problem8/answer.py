class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_search(node):
    unival_value = 0

    if node.left:
        unival_value += tree_search(node.left)
    
    if node.right:
        unival_value += tree_search(node.right)

    if not node.left and not node.right:
        return 1
    elif node.left.value == node.right.value:
        unival_value += 1
    
    return unival_value

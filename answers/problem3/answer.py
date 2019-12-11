class Node(object):
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    
    def load(self, value):
        if 'left' in value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.load(value)
        
        if 'right' in value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.load(value)


node_value_array = []
def serialize(node):
    node_value_array.append(node.val)

    if node.left:
        serialize(node.left)
    
    if node.right:
        serialize(node.right)

    return node_value_array

def deserialize(node_array):
    root_node = Node(node_array[0])
    del node_array[0]

    for node_value in node_array:
        root_node.load(node_value)
    
    return root_node
    


def main():
    pass



if __name__ == "__main__":
    main()
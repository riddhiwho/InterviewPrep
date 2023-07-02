'''In Python, you can represent a binary tree using classes and objects. 
Each node in the binary tree can be represented as an object, 
and each object contains references to its left and right child nodes (if any).
Here's an example implementation:'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

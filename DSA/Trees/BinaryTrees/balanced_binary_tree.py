class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def isBalanced(root):
        return (Height(root) >= 0)
def Height(root):
    if root is None:  return 0
    leftheight, rightheight = Height(root.left), Height(root.right)
    if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
    return max(leftheight, rightheight) + 1

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    # root.right.right = Node(7)
    root.right.left.left = Node(8)
    # root.right.left.left.right = Node(9)
    # root.right.left.left.right.right = Node(10)
    
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(2)
    # root.left.left = Node(3)
    # root.right.right = Node(3)
    # root.left.left.left = Node(4)
    # root.right.right.right = Node(4)
    print(isBalanced(root))
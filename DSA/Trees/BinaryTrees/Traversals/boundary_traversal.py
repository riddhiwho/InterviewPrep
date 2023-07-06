class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def printLeft(root):
    if root is None:
        return
    if root.left!=None:
        print(root.data, end=" ")
        printLeft(root.left)
    elif root.right is not None:
        print(root.data, end=" ")
        printLeft(root.right)
    
def printLeaves(root):
    if root is None:
        return 
    printLeaves(root.left)
    if root.left is None and root.right is None:
        print(root.data, end = " ")
    printLeaves()

    
def boundary(root):
    if root is None:
        return
    print(root.data, end = " ")
    printLeft(root.left)
    printLeaves(root.left)
    printRight(root.right)


if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    boundary(root)
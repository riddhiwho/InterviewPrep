'''
Pre: root left right
In: left root right
Post: left right root
'''

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
def printPreorder(root):
    if root:
        print(root.data, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right) 
        print(root.data, end=" ")      
        
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

# printPreorder(root)
# printInorder(root)
printPostorder(root)
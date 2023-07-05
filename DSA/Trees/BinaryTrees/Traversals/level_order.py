class Node:
    
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def level(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    queue.append(None)
    
    while len(queue)>0:
        node = queue.pop(0)
        if node is None:
            if len(queue)>0:
                print()
                queue.append(None)
            continue
        print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def printLevelOrder(root):
    if root is None:
        return

    queue = []
    
    queue.append(root)
    
    while len(queue)>0:
        print(queue[0].data, end = " ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # printLevelOrder(root)
    level(root)
    # zig(root)
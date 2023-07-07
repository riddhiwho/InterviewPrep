class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
def diam(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    queue.append(None)
    max_diam = 1
    stack = [root]
    
    while len(queue)>0:
        node = queue.pop(0)
        if node is None:
            if len(queue)>0:
                # print()
                queue.append(None)
                if len(stack)>max_diam:
                    max_diam = len(stack)
                stack = []
            continue
        # print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
            stack.append(node.left)
        if node.right is not None:
            queue.append(node.right)
            stack.append(node.right)
    
    return max_diam
        
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(3)
    root.left.left.left = Node(4)
    root.right.right.right = Node(4)
    print(diam(root))
    
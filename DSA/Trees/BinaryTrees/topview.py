class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def topView_level(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    queue.append(None)
    flag = False
    
    while len(queue)>0:
        node = queue[0]
        if node is None:
            flag = True
            queue.pop(0)
            if len(queue)>0:
                queue.append(None)
            continue
        if queue[1]==None or flag==True:
            print(node.data, end = " ")
        queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        
def level(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    queue.append(None)
    
    while len(queue)>0:
        node = queue[0]
        if node==None:
            queue.pop(0)
            if len(queue)>0:
                print()
                queue.append(None)
            continue
        else:
            if node.right==None or node.left==None:
                print(node.data, end = " ")
            node = queue.pop(0)
            
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
def top_left(root):
    if root is None:
        return
    top_left(root.left)
    print(root.data, end=" ")

def top_right(root):
    if root is None:
        return
    print(root.data, end=" ")
    top_right(root.right)
    
def top(root):
    if root is None:
        return
    top_left(root)
    if root.right!=None:
        top_right(root.right)

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(7)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    # top(root)
    topView_level(root)
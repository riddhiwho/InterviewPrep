class Node:
    
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    

def iter(root):
    if root==None:
        return
    
    stack=[]
    
    stack.append(root)
    
    while(len(stack)>0):
        curr=stack[-1]
        print(curr.data, end=" ")
        stack.pop()
        if curr.right!=None:
            stack.append(curr.right)
        if curr.left!=None:
            stack.append(curr.left)
        

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.left.left = Node(70)
root.left.right = Node(50)
root.right.left = Node(60)
root.left.left.right = Node(80)
 
iter(root)
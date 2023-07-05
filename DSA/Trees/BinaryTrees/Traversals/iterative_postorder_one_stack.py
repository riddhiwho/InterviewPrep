class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def postOrder(root):
    if root is None:
        return
    stack=[]
    curr=root
    while curr is not None or len(stack)>0:
        if curr is not None:
            stack.append(curr)
            curr=curr.left
        else:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                print(temp.data, end=" ")
                while len(stack)>0 and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.data, end=" ")
            else:
                curr=temp

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    postOrder(root)
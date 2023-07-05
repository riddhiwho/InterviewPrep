class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def zigzag(root):
    if root is None:
        return

    ans = []
    queue = [root]
    flag = False
    
    while len(queue)>0:
        n = len(queue)
        level = []
        for i in range(n):
            node = queue[0]
            queue.pop(0)
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if flag==False:
            level = level[::-1]
        for i in range(n):
            ans.append(level[i])
        flag = not flag
    return ans

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    ans = zigzag(root)
    for i in ans:
        print(i, end = " ")
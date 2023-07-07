class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


def dfs(root, depth):
    if not root: return depth
    return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

def maxDepth(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)
    queue.append(None)
    max_depth_tree = 1
    
    while len(queue)>0:
        node = queue.pop(0)
        if node is None:
            if len(queue)>0:
                queue.append(None)
                max_depth_tree+=1
            continue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    return max_depth_tree
    
    
    
    
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.left.left.right = Node(9)
    root.right.left.left.right.right = Node(10)
    # print(maxDepth(root))
    print(dfs(root, 0))
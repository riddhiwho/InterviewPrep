# Python code to implement the Level order traversal approach
from queue import Queue

# Definition of a Binary Tree Node
class Node:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

# Function to check if two trees are identical or not
def isIdentical(root1, root2):
	# Base case: if both roots are None, then trees are
	# identical
	if not root1 and not root2:
		return True

	# If one of the roots is None, then trees are not
	# identical
	if not root1 or not root2:
		return False

	# Create queues to perform level order traversal on
	# both trees
	q1 = Queue()
	q2 = Queue()

	# Add the roots of both trees to their respective
	# queues
	q1.put(root1)
	q2.put(root2)

	# Loop until either of the queues becomes empty
	while not q1.empty() and not q2.empty():
		# Get the front node from both queues
		curr1 = q1.get()
		curr2 = q2.get()

		# If the data of the current nodes is not equal,
		# then trees are not identical
		if curr1.data != curr2.data:
			return False

		# If the left child of one tree exists and the left
		# child of the other tree does not exist, then
		# trees are not identical
		if (curr1.left and not curr2.left) or (not curr1.left and curr2.left):
			return False

		# If the right child of one tree exists and the
		# right child of the other tree does not exist,
		# then trees are not identical
		if (curr1.right and not curr2.right) or (not curr1.right and curr2.right):
			return False

		# If both left and right children of both trees
		# exist, then add them to their respective queues
		if curr1.left and curr2.left:
			q1.put(curr1.left)
			q2.put(curr2.left)
		if curr1.right and curr2.right:
			q1.put(curr1.right)
			q2.put(curr2.right)

	# If we have reached this point, then trees are
	# identical
	return True

# Driver Code
if __name__ == '__main__':
	# Create the first tree
	root1 = Node(1)
	root1.left = Node(2)
	root1.right = Node(3)
	root1.left.left = Node(4)
	root1.left.right = Node(5)

	# Create the second tree
	root2 = Node(1)
	root2.left = Node(2)
	root2.right = Node(3)
	root2.left.left = Node(4)
	root2.left.right = Node(5)

	# Check if the trees are identical or not
	if isIdentical(root1, root2):
		print("The trees are identical")
	else:
		print("The trees are not identical")

#This code is contributed by shivamsharma215

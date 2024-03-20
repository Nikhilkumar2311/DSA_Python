# Program for tree traversal (preOrder, postOrder, inOrder)
"""
# Define a Node class to represent each node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to perform PreOrder traversal of the binary tree
def preOrder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preOrder(node.left)
    preOrder(node.right)


# Function to perform InOrder traversal of the binary tree
def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data, end=' ')
    inOrder(node.right)


# Function to perform PostOrder traversal of the binary tree
def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=' ')


# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Perform PreOrder traversal and print the result
print("PreOrder Traversal: ")
preOrder(root)

# Perform InOrder traversal and print the result
print("\nInOrder Traversal: ")
inOrder(root)

# Perform PostOrder traversal and print the result
print("\nPostOrder Traversal: ")
postOrder(root)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node.data, end=' ')
    inOrder(node.right)


def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("PreOrder Traversal: ")
preOrder(root)

print("\nInOrder Traversal: ")
inOrder(root)

print("\nPostOrder Traversal: ")
postOrder(root)
